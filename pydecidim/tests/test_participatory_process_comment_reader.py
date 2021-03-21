import unittest

from pydecidim.api.decidim_connector import DecidimConnector
from pydecidim.api.proposal_comment_reader import ProposalProcessCommentReader
from pydecidim.model.comment import Comment

QUERY_PATH = "https://www.decidim.barcelona/api"


class ProposalCommentReaderTest(unittest.TestCase):
    def test_execute_not_exists(self):
        decidim_connector: DecidimConnector = DecidimConnector(QUERY_PATH)
        reader: ProposalProcessCommentReader \
            = ProposalProcessCommentReader(decidim_connector, base_path="../..", participatory_space_name="assembly")
        # We use the participatory process #5 on Decidim.org api and the Proposal #12040
        comment: Comment = reader.execute("318", "22520", "2")
        self.assertIsNone(comment)

    def test_execute_exists(self):
        decidim_connector: DecidimConnector = DecidimConnector(QUERY_PATH)
        reader: ProposalProcessCommentReader \
            = ProposalProcessCommentReader(decidim_connector, base_path="../..", participatory_space_name="assembly")
        # We use the participatory space #5 on Decidim.org api and the Proposal #12888
        comment: Comment = reader.execute("318", "22520", "25546")
        self.assertIsInstance(comment, Comment)


if __name__ == '__main__':
    unittest.main()
