import csv
import time
from typing import Dict

from api.comment_reader import CommentReader
from api.decidim_connector import DecidimConnector
from api.participatory_processes_reader import ParticipatoryProcessesReader
from api.proposal_reader import ProposalReader
from api.proposals_reader import ProposalsReader
from model.CommentTreeElement import CommentTreeElement
from model.comment import Comment

API_URL = "https://meta.decidim.org/api"
decidim_connector = DecidimConnector(API_URL)
# version_reader = VersionReader(decidim_connector)
# version = version_reader.process_query()
# print(version)

filename = "output.csv"
SLEEPING_TIME = 10

participatory_processes_reader = ParticipatoryProcessesReader(decidim_connector)
participatory_processes = participatory_processes_reader.execute()

proposals_reader = ProposalsReader(decidim_connector)
proposal_reader = ProposalReader(decidim_connector)
comment_reader = CommentReader(decidim_connector)

csv_header_list = ["participatory_process_id",
                   "proposal_id",
                   "comment_id",
                   "comment_parent",
                   "comment_children",
                   "comment",
                   "comment_alignment",
                   "comment_upvotes",
                   "comment_downvotes"]

dict_of_comments: Dict[str, Comment] = dict()
root_node: CommentTreeElement = CommentTreeElement(None, None)


def explore_comment_hierarchy(comment_id: str,
                              parent: CommentTreeElement,
                              participatory_process_id:
                              str, proposal_id: str,
                              current_level=0):
    comment_full_info = comment_reader.execute(
        participatory_process_id,
        proposal_id,
        comment_id
    )

    print("\t\t{}|-Comment #{} retrieved".format("\t" * current_level, comment_id))
    node_tree: CommentTreeElement = CommentTreeElement(comment_full_info, parent)
    dict_of_comments[comment_id] = comment_full_info
    children_ids = comment_full_info.comments_id
    for children_id in children_ids:
        explore_comment_hierarchy(children_id, node_tree, participatory_process_id, proposal_id, current_level + 1)
        time.sleep(SLEEPING_TIME)


def export_comment_hierarchy(writer,
                             csv_header_list,
                             node,
                             participatory_process_id,
                             proposal_id
                             ):
    if not node.is_root():
        new_row = [participatory_process_id,
                   proposal_id,
                   node.comment.comment_id,
                   node.parent.comment.comment_id if not node.parent.is_root() else "",
                   ','.join([child.comment.comment_id for child in node.childrens]),
                   node.comment.body,
                   node.comment.alignment,
                   node.comment.up_votes,
                   node.comment.down_votes
                   ]
        writer.writerow(new_row)
    for child in node.childrens:
        export_comment_hierarchy(writer, csv_header_list, child, participatory_process_id, proposal_id)


csvfile = open(filename, "w")
writer = csv.writer(csvfile, delimiter=',')
writer.writerow(csv_header_list)

for partipatory_process in participatory_processes:
    print("Analyzing participatory process #{}".format(partipatory_process))
    proposals_list = proposals_reader.execute(partipatory_process)
    for proposal in proposals_list:
        proposal_full_info = proposal_reader.execute(partipatory_process, proposal)
        print("\t|-Analyzing proposal #{}".format(proposal_full_info.proposal_id))
        time.sleep(SLEEPING_TIME)
        if proposal_full_info.has_comments:
            for comment_id in proposal_full_info.comments_ids:
                explore_comment_hierarchy(comment_id, root_node, partipatory_process, proposal)
                comment_full_info = comment_reader.execute(
                    partipatory_process,
                    proposal,
                    comment_id
                )
                export_comment_hierarchy(writer, csv_header_list, root_node, partipatory_process, proposal)
                root_node = CommentTreeElement(None, None)
                dict_of_comments.clear()
                csvfile.flush()
                time.sleep(SLEEPING_TIME)

csvfile.close()
