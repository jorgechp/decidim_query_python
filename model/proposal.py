from typing import List

from model.Comment import Comment
from model.abstract_api_element import AbstractApiElement


class Proposal(AbstractApiElement):
    """
    Represents a Participatory Process from the Decidim API.
    """

    def __init__(self, proposal_id: str, totalCommentsCount: int, title: str, comments: List[Comment]) -> None:
        pass




