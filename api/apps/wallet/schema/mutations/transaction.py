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

class AddTransaction(graphene.Mutation):
    """
    Add Transaction Mutation (Traditional)

    Args:
        new_transaction (obj): transaction object data
    Returns:
        success (str): success message
        transaction (obj): new transaction instance
    Raises:
        errors (obj): error object response
    """
    success = graphene.String()
    transaction = graphene.Field(TransactionType)

    class Arguments:
        new_transaction = graphene.Argument(TransactionInputType)

    @classmethod
    def mutate(self, root, info):
        try:
            transaction_instance = Transaction(**new_transaction)
        except Exception:
            raise GraphQLError(ERROR_RESPONSES['something_wrong'])
        with SaveContextManager(transaction_instance, model=Transaction) as transaction:
            return AddTransaction(success=SUCCESS_RESPONSES['creation_success'].format('Transaction'), transaction=transaction)
