import unittest

from api.decidim_connector import DecidimConnector
from api.version_reader import VersionReader

API_URL = "https://meta.decidim.org/api"


class VersionReaderTest(unittest.TestCase):
    def test_process_query(self):
        decidim_connector: DecidimConnector = DecidimConnector(API_URL)
        version_reader: VersionReader = VersionReader(decidim_connector,  base_path="..")
        version = version_reader.process_query()
        self.assertIsInstance(version, str)


if __name__ == '__main__':
    unittest.main()
