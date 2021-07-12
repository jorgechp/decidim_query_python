from __future__ import annotations

from typing import Dict, List

from pydecidim.model.abstract_api_element import AbstractApiElement


class PageInfo(AbstractApiElement):
    """
    Represents a Page Info from the Decidim API.
    """

    @property
    def end_cursor(self) -> str:
        return self.__end_cursor

    @property
    def start_cursor(self) -> str:
        return self.__start_cursor

    @property
    def has_previous_page(self) -> bool:
        return self.__has_previous_page

    @property
    def has_next_page(self) -> bool:
        return self.__has_next_page

    @staticmethod
    def parse_from_gql(gql_list: List[dict]) -> PageInfo:
        translation_dict: Dict[str, str] = gql_list[0]
        end_cursor: str = translation_dict['endCursor']
        start_cursor: str = translation_dict['startCursor']
        has_previous_page: bool = translation_dict['hasPreviousPage']
        has_next_page: bool = translation_dict['hasNextPage']
        return PageInfo(end_cursor, start_cursor, has_previous_page, has_next_page)

    def __init__(self,
                 end_cursor: str,
                 start_cursor: str,
                 has_previous_page: bool,
                 has_next_page: bool):
        self.__end_cursor: str = end_cursor
        self.__start_cursor: str = start_cursor
        self.__has_previous_page: bool = has_previous_page
        self.__has_next_page: bool = has_next_page
