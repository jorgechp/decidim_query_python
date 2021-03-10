from api.complex.get_all_comments_from_proposals_reader import GetAllCommentsFromProposalsReader
from api.decidim_connector import DecidimConnector

API_URL = "https://meta.decidim.org/api"

decidim_connector = DecidimConnector(API_URL)
all_comments_reader = GetAllCommentsFromProposalsReader(decidim_connector)
all_comments_reader.execute(depth=6)
