import graphene
from graphene_django_extras import DjangoSerializerMutation
from graphql import GraphQLError

from api.apps.wallet.schema.types import TransactionType, TransactionInputType
from api.apps.wallet.models import Transaction
from api.utils.database import SaveContextManager, get_model_object
from api.apps.wallet.serializers import TransactionSerializer
from api.utils.common_responses import SUCCESS_RESPONSES, ERROR_RESPONSES

class TransactionSerializerMutation(DjangoSerializerMutation):
    """
    DjangoSerializerMutation auto-implements Create, Delete, and Update functions
    """
    class Meta:
        description = "DRF serializer-based Mutation for Transactions"
        serializer_class = TransactionSerializer
