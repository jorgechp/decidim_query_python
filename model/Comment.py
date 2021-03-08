from __future__ import annotations

from typing import List
from model.abstract_api_element import AbstractApiElement



class Comment(AbstractApiElement):
    """
    Represents a Participatory Process from the Decidim API.
    """

    def __init__(self, body: str, alignment: int, comments: List[Comment], down_votes: int, up_votes: int) -> None:
        self._body: str = body
        self._aligment: int = alignment
        self._comments: List[Comment] = comments
        self._down_votes: int = down_votes
        self.up_votes: int = up_votes