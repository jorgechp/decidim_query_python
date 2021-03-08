from api.comment_reader import CommentReader
from api.decidim_connector import DecidimConnector
from api.participatory_processes_reader import ParticipatoryProcessesReader
from api.proposal_reader import ProposalReader
from api.proposals_reader import ProposalsReader

API_URL = "https://meta.decidim.org/api"
decidim_connector = DecidimConnector(API_URL)
# version_reader = VersionReader(decidim_connector)
# version = version_reader.process_query()
# print(version)

participatory_processes_reader = ParticipatoryProcessesReader(decidim_connector)
participatory_processes = participatory_processes_reader.process_query()

proposals_reader = ProposalsReader(decidim_connector)
proposal_reader = ProposalReader(decidim_connector)
comment_reader = CommentReader(decidim_connector)

for partipatory_process in participatory_processes:
    proposals_list = proposals_reader.process_query(partipatory_process)
    for proposal in proposals_list:
        proposal_full_info = proposal_reader.process_query(partipatory_process, proposal)
        if proposal_full_info.has_comments:
            for comment_id in proposal_full_info.comments_ids:
                comment_full_info = comment_reader.process_query(
                    partipatory_process,
                    proposal,
                    comment_id
                )






