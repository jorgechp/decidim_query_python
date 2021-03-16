"""
This Reader retrives a full Proposal information.
"""

from pydecidim.api.decidim_connector import DecidimConnector
from pydecidim.api.proposal_comment_reader import ProposalProcessCommentReader

# Path to the query schema

QUERY_PATH = 'pydecidim/queries/assemblies_comment.graphql'


class AssembliesProcessCommentReader(ProposalProcessCommentReader):
    """
    This reader retrieves a Proposal from Decidim.
    """

    def __init__(self, decidim_connector: DecidimConnector, base_path="."):
        """

        :param decidim_connector: An instance of a DecidimConnector class.
        :param base_path: The base path to the schema directory.
        """
        super().__init__(query_path=QUERY_PATH, decidim_connector=decidim_connector, base_path=base_path + "/")
