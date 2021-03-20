from pydecidim.api.abstract_decidim_reader import AbstractDecidimReader
from pydecidim.api.decidim_connector import DecidimConnector


class ParticipatorySpaceReader(AbstractDecidimReader):

    @property
    def participatory_space_name(self):
        return self.__participatory_space_name

    def __init__(self, decidim_connector: DecidimConnector, participatory_space_name: str, query_schema: str):
        super().__init__(decidim_connector, query_schema)
        self.__participatory_space_name = participatory_space_name
