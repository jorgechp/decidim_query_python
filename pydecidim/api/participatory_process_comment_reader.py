"""
This Reader retrives a full Proposal information.
"""

from pydecidim.api.decidim_connector import DecidimConnector
from pydecidim.api.proposal_comment_reader import ProposalProcessCommentReader
from pydecidim.model.comment import Comment
from pydecidim.model.elemental_type_element import ElementalTypeElement

# Path to the query schema

QUERY_PATH = 'pydecidim/queries/participatory_process_comment.graphql'


class ParticipatoryProcessCommentReader(ProposalProcessCommentReader):
    """
    This reader retrieves a Proposal from Decidim.
    """

    def __init__(self, decidim_connector: DecidimConnector, base_path="."):
        """

        :param decidim_connector: An instance of a DecidimConnector class.
        :param base_path: The base path to the schema directory.
        """
        super().__init__(query_path=QUERY_PATH,
                         decidim_connector=decidim_connector,
                         participatory_space_name='participatoryProcess',
                         base_path=base_path + "/")
