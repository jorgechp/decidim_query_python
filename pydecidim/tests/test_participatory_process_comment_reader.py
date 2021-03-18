import unittest

from pydecidim.api.decidim_connector import DecidimConnector
from pydecidim.api.participatory_process_comment_reader import ParticipatoryProcessCommentReader
from pydecidim.model.comment import Comment

QUERY_PATH = "https://www.decidim.barcelona/api"


class ProposalReaderTest(unittest.TestCase):
    def test_execute_not_exists(self):
        decidim_connector: DecidimConnector = DecidimConnector(QUERY_PATH)
        reader: ParticipatoryProcessCommentReader \
            = ParticipatoryProcessCommentReader(decidim_connector, base_path="../..")
        # We use the participatory process #5 on Decidim.org api and the Proposal #12040
        comment: Comment = reader.execute("5", "12040", "2")
        self.assertIsNone(comment)

    def test_execute_exists(self):
        decidim_connector: DecidimConnector = DecidimConnector(QUERY_PATH)
        reader: ParticipatoryProcessCommentReader \
            = ParticipatoryProcessCommentReader(decidim_connector, base_path="../..")
        # We use the participatory space #5 on Decidim.org api and the Proposal #12888
        comment: Comment = reader.execute("5", "12888", "20287")
        self.assertIsInstance(comment, Comment)


if __name__ == '__main__':
    unittest.main()
