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
