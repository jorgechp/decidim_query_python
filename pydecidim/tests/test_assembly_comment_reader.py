import unittest

from pydecidim.api.assemblies_comment_reader import AssembliesCommentReader
from pydecidim.api.decidim_connector import DecidimConnector
from pydecidim.model.comment import Comment

QUERY_PATH = "https://www.decidim.barcelona/api"


class AssemblyCommentReaderTest(unittest.TestCase):
    def test_execute_not_exists(self):
        decidim_connector: DecidimConnector = DecidimConnector(QUERY_PATH)
        reader: AssembliesCommentReader \
            = AssembliesCommentReader(decidim_connector, base_path="../..")
        # We use the assembly #318 on Decidim.org api and the Proposal #22520, comment #2 (not exists)
        comment: Comment = reader.execute("318", "22520", "2")
        self.assertIsNone(comment)

    def test_execute_exists(self):
        decidim_connector: DecidimConnector = DecidimConnector(QUERY_PATH)
        reader: AssembliesCommentReader \
            = AssembliesCommentReader(decidim_connector, base_path="../..")
        # We use the assembly #318 on Decidim.org api and the Proposal #22520, comment #25546
        comment: Comment = reader.execute("318", "22520", "25546")
        self.assertIsInstance(comment, Comment)


if __name__ == '__main__':
    unittest.main()
