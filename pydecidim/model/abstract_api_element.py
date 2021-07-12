"""
This file contains the definition of the abstract class AbstractApiElement. Which is the common parent of
all othe classes from the model.
"""
from __future__ import annotations

from abc import ABC


class AbstractApiElement(ABC):
    """
    The abstract class AbstractApiElement define methods to parse information from the GraphQL API.
    """

    def parse_arguments_to_gql(self) -> str:
        """
        Returns a string with the format of GraphQL arguments.
        :return: A string in GraphQL format.
        """
        pass

    def parse_from_gql(self) -> AbstractApiElement:
        """
        Returns an AbstractApiElement instance from a GraphQL dictionary.
        :return: An AbstractApiElement instnace
        """
        pass
