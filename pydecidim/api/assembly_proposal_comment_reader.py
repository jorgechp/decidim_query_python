"""
This Reader retrives a full Proposal information.
"""
from pydecidim.api.decidim_connector import DecidimConnector
from pydecidim.api.proposal_comment_reader import ProposalProcessCommentReader

# Path to the query schema

QUERY_PATH = 'pydecidim/queries/assembly_comment.graphql'


class AssemblyProposalCommentReader(ProposalProcessCommentReader):
    """
    This reader retrieves a Proposal from Decidim.
    """

    def __init__(self,
                 decidim_connector: DecidimConnector,
                 participatory_space_name: str,
                 base_path="."):
        """

        :param decidim_connector: An instance of a DecidimConnector class.
        :param base_path: The base path to the schema directory.
        """
        super().__init__(decidim_connector, participatory_space_name, base_path + "/" + QUERY_PATH)
