"""
This Reader retrives a list of Proposals from Decidim.
"""
import time
from typing import List

from pydecidim.api.decidim_connector import DecidimConnector
from pydecidim.api.participatory_space_name_enum import ParticipatorySpaceNameEnum
from pydecidim.api.participatory_space_reader import ParticipatorySpaceReader
from pydecidim.model.elemental_type_element import ElementalTypeElement
# Path to the query schema
from pydecidim.model.page_info import PageInfo

QUERY_PATH = 'pydecidim/queries/proposals.graphql'
QUERY_PATH_WITH_CURSOR = 'pydecidim/queries/proposals_with_cursor.graphql'


class ProposalsReader(ParticipatorySpaceReader):
    """
    This reader retrieves list of Proposals from Decidim.
    """

    def __init__(self, decidim_connector: DecidimConnector,
                 participatory_space_name: ParticipatorySpaceNameEnum,
                 base_path="."):
        """

        :param decidim_connector: An instance of a DecidimConnector class.
        :param base_path: The base path to the schema directory.
        """
        super().__init__(decidim_connector, participatory_space_name, base_path + "/" + QUERY_PATH)
        self.__base_path: str = base_path

    def execute(self, participatory_process_id: str) -> List[str]:
        """
        Send the query to the API and extract a list of proposals ids from a participatory space.
        :param participatory_process_id: The participatory process id.
        :return: A list of proposals ids.
        """

        has_next_page: bool = True
        cursor: str or None = ''
        proposals_id: List[str] = []

        while has_next_page:
            response: dict = super().process_query_from_file({
                'id': ElementalTypeElement(participatory_process_id),
                'PARTICIPATORY_SPACE_NAME': ElementalTypeElement(super().participatory_space_name.value),
                'after': ElementalTypeElement(cursor),
            })

            components = response[super().participatory_space_name.value]['components']
            if len(components) > 0:
                component = response[super().participatory_space_name.value]['components'][0]
                page_info: PageInfo = PageInfo.parse_from_gql([component['proposals']['pageInfo']])
                has_next_page = page_info.has_next_page
                cursor = page_info.end_cursor

                for proposal_dict in component['proposals']['edges']:
                    proposal_id: str = proposal_dict['node']['id']
                    proposals_id.append(proposal_id)

                if has_next_page:
                    self.query_path = self.__base_path + "/" + QUERY_PATH_WITH_CURSOR
                    time.sleep(10)
        return proposals_id
