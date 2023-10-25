import graphene
from graphene_django_extras import DjangoSerializerMutation
from graphql import GraphQLError

from api.apps.wallet.schema.types import WalletType, WalletInputType
from api.apps.wallet.models import Wallet
from api.utils.database import SaveContextManager, get_model_object
from api.apps.wallet.serializers import WalletSerializer
from api.utils.common_responses import SUCCESS_RESPONSES, ERROR_RESPONSES

class WalletSerializerMutation(DjangoSerializerMutation):
    """
    DjangoSerializerMutation auto-implements Create, Delete, and Update functions
    """
    class Meta:
        description = "DRF serializer-based Mutation for Wallets"
        serializer_class = WalletSerializer

class AddWallet(graphene.Mutation):
    """
    Add Wallet Mutation (Traditional)

    Args:
        new_wallet (obj): wallet object data
    Returns:
        success (str): success message
        wallet (obj): new wallet instance
    Raises:
        errors (obj): error object response
    """
    success = graphene.String()
    wallet = graphene.Field(WalletType)

    class Arguments:
        new_wallet = graphene.Argument(WalletInputType)

    @classmethod
    def mutate(cls, root, info, new_wallet: dict) -> 'AddWallet':
        try:
            wallet_instance = Wallet(**new_wallet)
        except Exception:
            raise GraphQLError(ERROR_RESPONSES['something_wrong'])
        with SaveContextManager(wallet_instance, model=Wallet) as wallet:
            return cls(success=SUCCESS_RESPONSES['creation_success'].format('Wallet'))
