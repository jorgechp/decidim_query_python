import time
from typing import List, Dict

from api.comment_reader import CommentReader
from api.decidim_connector import DecidimConnector
from api.participatory_processes_reader import ParticipatoryProcessesReader
from api.proposal_reader import ProposalReader
from api.proposals_reader import ProposalsReader
from model.comment import Comment

API_URL = "https://meta.decidim.org/api"
decidim_connector = DecidimConnector(API_URL)
# version_reader = VersionReader(decidim_connector)
# version = version_reader.process_query()
# print(version)

participatory_processes_reader = ParticipatoryProcessesReader(decidim_connector)
participatory_processes = participatory_processes_reader.execute()

proposals_reader = ProposalsReader(decidim_connector)
proposal_reader = ProposalReader(decidim_connector)
comment_reader = CommentReader(decidim_connector)

csv_header_list = ["participatory_process_id",
                   "proposal_id",
                   "proposal_name",
                   "comment_id",
                   "comment",
                   "comment_alignment",
                   "comment_upvotes",
                   "comment_downvotes"]

dict_of_comments_hierarchy: Dict[str, List[str]] = dict()
dict_of_dictionaries: Dict[str, Comment] = dict()


def explore_comment_hierarchy(comment_id: str, participatory_process_id: str, proposal_id: str):
    comment_full_info = comment_reader.execute(
        participatory_process_id,
        proposal_id,
        comment_id
    )
    dict_of_dictionaries[comment_id] = comment_full_info
    children_ids = comment_full_info.comments_id
    dict_of_comments_hierarchy[comment_id] = children_ids
    for children_id in children_ids:
        explore_comment_hierarchy(children_id, participatory_process_id, proposal_id)
        time.sleep(3)


for partipatory_process in participatory_processes:
    proposals_list = proposals_reader.execute(partipatory_process)
    for proposal in proposals_list:
        proposal_full_info = proposal_reader.execute(partipatory_process, proposal)
        time.sleep(3)
        if proposal_full_info.has_comments:
            for comment_id in proposal_full_info.comments_ids:
                explore_comment_hierarchy(comment_id, partipatory_process, proposal)

                comment_full_info = comment_reader.execute(
                    partipatory_process,
                    proposal,
                    comment_id
                )
                print(comment_full_info)
                time.sleep(3)






