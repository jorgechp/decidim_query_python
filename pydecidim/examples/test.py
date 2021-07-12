from pydecidim.api.decidim_connector import DecidimConnector
from pydecidim.api.participatory_space_name_enum import ParticipatorySpaceNameEnum
from pydecidim.api.participatory_spaces_reader import ParticipatorySpacesReader
from pydecidim.api.proposals_reader import ProposalsReader

QUERY_PATH = "https://www.decidim.barcelona/api"
decidim_connector = DecidimConnector(QUERY_PATH)
processes = ParticipatorySpacesReader(decidim_connector,
                                      participatory_space_name=ParticipatorySpaceNameEnum.PARTICIPATORY_PROCESSES,
                                      base_path="../..")

procs = processes.execute()

print('79' in procs)

proposals_reader = ProposalsReader(decidim_connector,
                                   participatory_space_name=ParticipatorySpaceNameEnum.PARTICIPATORY_PROCESS,
                                   base_path="../..")

count = 0
for id in procs:
    proposals_list = proposals_reader.execute(id)
    count += len(proposals_list)
    print(count)

print(count)
