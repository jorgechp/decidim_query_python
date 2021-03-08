from __future__ import annotations

from typing import List
from model.abstract_api_element import AbstractApiElement


class Comment(AbstractApiElement):
    """
    Represents a Participatory Process from the Decidim API.
    """

    @staticmethod
    def parse_from_gql(comment_dict: dict) -> Comment:
        """
        Parses a comment from gql to a Comment instance.

        :param comment_dict: The dict with the Comment information.
        :return: A Comment
        """
        pass

    @property
    def body(self) -> str:
        return self.__body

    @property
    def alignment(self) -> int:
        return self.__alignment

    @property
    def comments_id(self) -> List[str]:
        return self.__comments_id

    @property
    def down_votes(self) -> int:
        return self.__down_votes

    @property
    def up_vote(self) -> int:
        return self.__up_votes

    def __init__(self, body: str, alignment: int, down_votes: int, up_votes: int, comments_id: List[str]) -> None:
        self.__body: str = body
        self.__alignment: int = alignment
        self.__down_votes: int = down_votes
        self.__up_votes: int = up_votes
        self.__comments_id: List[str] = comments_id


