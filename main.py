from api.decidim_connector import DecidimConnector
from api.participatory_processes_reader import ParticipatoryProcessesReader
from api.version_reader import VersionReader

API_URL = "https://meta.decidim.org/api"
decidim_connector = DecidimConnector(API_URL)
version_reader = VersionReader(decidim_connector)
version = version_reader.process_query()
print(version)

participatory_processes_reader = ParticipatoryProcessesReader(decidim_connector)
participatory_processes = participatory_processes_reader.process_query()
