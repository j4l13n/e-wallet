import graphene
from graphene_django_extras import DjangoSerializerMutation
from graphql import GraphQLError

from api.apps.wallet.schema.types import WalletType, WalletInputType
from api.apps.wallet.models import Wallet
from api.apps.authenticate.models import User
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

    def mutate(self, info, **kwargs):
        try:
            new_wallet = kwargs.get('new_wallet')
            wallet_data = {}
            
            for key, value in new_wallet.items():
                if key == 'customer' and value:
                    customer_instance = get_model_object(User, 'id', value)
                    wallet_data[key] = customer_instance
                else:
                    if value:
                            wallet_data[key] = value
            wallet_instance = Wallet(**wallet_data)

            with SaveContextManager(wallet_instance, model=Wallet) as wallet:
                success = SUCCESS_RESPONSES['create_success'].format('Wallet')
                return AddWallet(success=success, wallet=wallet)
        except Exception as e:
            raise GraphQLError(ERROR_RESPONSES['something_wrong'])
