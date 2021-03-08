import unittest

from api.decidim_connector import DecidimConnector
from api.proposal_reader import ProposalReader
from model.proposal import Proposal

API_URL = "https://meta.decidim.org/api"


class ProposalReaderTest(unittest.TestCase):
    def test_process_query_not_exists(self):
        decidim_connector: DecidimConnector = DecidimConnector(API_URL)
        reader: ProposalReader = ProposalReader(decidim_connector,  base_path="..")
        # We use the participatory process #40 on Decidim.org api and the Proposal #12040
        proposal: Proposal = reader.process_query(40, 1)
        self.assertIsNone(proposal)

    def test_process_query(self):
        decidim_connector: DecidimConnector = DecidimConnector(API_URL)
        reader: ProposalReader = ProposalReader(decidim_connector,  base_path="..")
        # We use the participatory process #40 on Decidim.org api and the Proposal #12040
        proposal: Proposal = reader.process_query(40, 12040)
        self.assertIsInstance(proposal, Proposal)


if __name__ == '__main__':
    unittest.main()
