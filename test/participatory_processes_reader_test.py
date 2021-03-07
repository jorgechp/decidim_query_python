import unittest
from typing import List

from api.decidim_connector import DecidimConnector
from api.participatory_processes_reader import ParticipatoryProcessesReader
from model.participatory_process import ParticipatoryProcess

API_URL = "https://meta.decidim.org/api"


class ParticipatoryProcessesReaderTest(unittest.TestCase):
    def test_process_query(self):
        decidim_connector: DecidimConnector = DecidimConnector(API_URL)
        reader: ParticipatoryProcessesReader = ParticipatoryProcessesReader(decidim_connector,  base_path="..")
        participatory_processes = reader.process_query()
        self.assertIsInstance(participatory_processes, List)
        if len(participatory_processes) > 0:
            self.assertIsInstance(participatory_processes[0], ParticipatoryProcess)


if __name__ == '__main__':
    unittest.main()
