from model.abstract_api_element import AbstractApiElement
from model.translated_field import TranslatedField


class ParticipatoryProcess(AbstractApiElement):
    """
    Represents a Participatory Process from the Decidim API.
    """

    @property
    def id(self) -> str:
        return self.__id

    @property
    def title(self) -> TranslatedField:
        return self.__title

    def __init__(self, title: TranslatedField, process_id: str) -> None:
        self.__id: str = process_id
        self.__title: TranslatedField = title
