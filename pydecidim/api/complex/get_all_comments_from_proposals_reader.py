"""
This Reader retrives a full Proposal information.
"""
import os
import pickle
from pathlib import Path
from typing import List, Dict

from pydecidim.api.abstract_decidim_reader import AbstractDecidimReader
from pydecidim.api.decidim_connector import DecidimConnector
from pydecidim.model import CommentTreeElement
from pydecidim.model.comment import Comment
# Path to the query schema
from pydecidim.model.translated_field import TranslatedField

QUERY_PATH = 'pydecidim/queries/complex/get_all_comments_from_proposals/get_all_comments_from_proposals.graphql'
RECURSIVE_FRAGMENT = 'queries/complex/get_all_comments_from_proposals/get_all_comments_from_proposals--recursive-fragment.graphql'


class GetAllCommentsFromProposalsReader(AbstractDecidimReader):
    """
    This reader retrieves a Proposal from Decidim.
    """

    def __init__(self, decidim_connector: DecidimConnector, base_path="."):
        """

        :param decidim_connector: An instance of a DecidimConnector class.
        :param base_path: The base path to the schema directory.
        """
        super().__init__(decidim_connector, base_path + "/" + QUERY_PATH)

    def __explore_comments_hierarchy(self, comment, parent_node: CommentTreeElement):
        comment_id = comment['id']
        comment_alignment = comment['alignment']
        comment_body = comment['body']
        comment_type = comment['type']
        comment_created_at = comment['createdAt']
        comment_down_votes = comment['downVotes']
        comment_up_votes = comment['upVotes']
        comments = comment['comments']

        new_comment = Comment(comment_id,
                              comment_body,
                              comment_alignment,
                              comment_created_at,
                              comment_down_votes,
                              comment_up_votes,
                              comment_type,
                              comments)

        new_node = CommentTreeElement(new_comment, parent_node)
        for children in comments:
            self.__explore_comments_hierarchy(children, new_node)

    def execute(self, depth: int) -> List[Comment] or None:
        """
        Send the query to the API and extract all the comments from
        :param depth: The participatory process id.
        :return: A list of comments.
        """

        if not os.path.isfile("response.csv"):
            file_content: str = Path(QUERY_PATH).read_text()
            file_recursive_content: str = Path(RECURSIVE_FRAGMENT).read_text()

            achieved_depth: int = 0
            while achieved_depth < depth:
                file_content = file_content.replace("%RECURSIVE_HIERARCHY%", file_recursive_content)
                achieved_depth += 1
            file_content = file_content.replace("%RECURSIVE_HIERARCHY%", '')
            response = super().process_query(file_content)
            pickle.dump(response, open("response.csv", "wb"))
        else:
            response = pickle.load(open("response.csv", "rb"))

        list_of_participatory_processes = response['participatoryProcesses']

        dict_of_participatory_processes: Dict[str, Dict[str, List[CommentTreeElement]]] = dict()

        for participatory_process in list_of_participatory_processes:
            process_id = participatory_process['id']
            created_at = participatory_process['createdAt']
            title = TranslatedField.parse_arguments_to_gql(participatory_process['title']['translations'])
            list_of_proposals = participatory_process['components'][0]['proposals']['edges']
            dict_of_participatory_processes[process_id]: Dict[str, List[str]] = dict()

            for proposal in list_of_proposals:
                proposal_info = proposal['node']
                proposal_id = proposal_info['id']
                proposal_title = TranslatedField.parse_arguments_to_gql(proposal_info['title'])
                proposal_created_at = proposal_info['createdAt']
                proposal_comments = proposal_info['comments']

                comment_root_node = CommentTreeElement(None, None)
                dict_of_participatory_processes[process_id][proposal_id] = comment_root_node

                for comment in proposal_comments:
                    comment_hierarchy_info = comment['comments']
                    for comment_info in comment_hierarchy_info:
                        self.__explore_comments_hierarchy(comment_info, comment_root_node)
        return dict_of_participatory_processes
