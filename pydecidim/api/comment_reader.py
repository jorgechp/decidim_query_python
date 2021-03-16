"""
This Reader retrives a full Proposal information.
"""

from pydecidim.api.abstract_decidim_reader import AbstractDecidimReader
from pydecidim.api.decidim_connector import DecidimConnector
from pydecidim.model.author import Author
from pydecidim.model.comment import Comment
from pydecidim.model.elemental_type_element import ElementalTypeElement

# Path to the query schema

QUERY_PATH = 'pydecidim/queries/comment.graphql'


class CommentReader(AbstractDecidimReader):
    """
    This reader retrieves a Proposal from Decidim.
    """

    def __init__(self, decidim_connector: DecidimConnector, base_path="."):
        """

        :param decidim_connector: An instance of a DecidimConnector class.
        :param base_path: The base path to the schema directory.
        """
        super().__init__(decidim_connector, base_path + "/" + QUERY_PATH)

    def execute(self, participatory_process_id: str, proposal_id: str, comment_id: str) -> Comment or None:
        """
        Send the query to the API and extract a list of proposals ids from a participatory space.
        :param participatory_process_id: The participatory process id.
        :param proposal_id: The proposal id.
        :param comment_id: The id of the comment to retrieve.
        :return: A list of proposals ids.
        """

        response: dict = super().process_query_from_file(
            {
                'ID_PARTICIPATORY_PROCESS': ElementalTypeElement(participatory_process_id),
                'ID_PROPOSAL': ElementalTypeElement(proposal_id),
                'ID_COMMENT': ElementalTypeElement(comment_id),
            })

        try:
            comment_dict = response['participatoryProcess']['components'][0]['proposal']['comments'][0]
            accepts_new_comments: bool = comment_dict['acceptsNewComments']
            alignment: int = comment_dict['alignment']
            already_reported: bool = comment_dict['alreadyReported']
            author: Author = Author.parse_from_gql(comment_dict['author'])
            body: str = comment_dict['body']
            comments_have_alignment: bool = comment_dict['commentsHaveAlignment']
            comments_have_votes: bool = comment_dict['commentsHaveVotes']
            created_at: str = comment_dict['createdAt']
            formatted_body: str = comment_dict['formattedBody']
            formatted_created_at: str = comment_dict['formattedCreatedAt']
            has_comments: bool = comment_dict['hasComments']
            sgid: str = comment_dict['sgid']
            total_comments_count: int = comment_dict['totalCommentsCount']
            comment_type: str = comment_dict['type']
            down_votes: int = comment_dict['downVotes']
            up_votes: int = comment_dict['upVotes']
            user_allowed_to_comment: bool = comment_dict['userAllowedToComment']
            comments_id_list = comment_dict['comments']

            comments_id = []
            for comment_id in comments_id_list:
                comments_id.append(comment_id['id'])

            new_comment: Comment = Comment(accepts_new_comments,
                                           alignment,
                                           already_reported,
                                           author,
                                           body,
                                           comments_have_alignment,
                                           comments_have_votes,
                                           created_at,
                                           formatted_body,
                                           formatted_created_at,
                                           has_comments,
                                           comment_id,
                                           sgid,
                                           total_comments_count,
                                           comment_type,
                                           down_votes,
                                           up_votes,
                                           user_allowed_to_comment,
                                           comments_id)
            return new_comment
        except IndexError:
            return None
