import graphene
from graphene_django_extras import DjangoSerializerMutation
from graphql import GraphQLError

from api.apps.wallet.schema.types import TransactionType, TransactionInputType
from api.apps.wallet.models import Transaction, Wallet
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

    def mutate(self, info, **kwargs):
        try:
            new_transaction = kwargs.get('new_transaction')
            transaction_data = {}

            for key, value in new_transaction.items():
                if key == 'source_wallet' and value:
                    wallet_instance = get_model_object(Wallet, 'id', value)
                    transaction_data[key] = wallet_instance
                elif key == 'destination_wallet' and value:
                    wallet_instance = get_model_object(Wallet, 'id', value)
                    transaction_data[key] = wallet_instance
                else:
                    if value:
                        transaction_data[key] = value
            transaction_instance = Transaction(**transaction_data)
            with SaveContextManager(transaction_instance, model=Transaction) as transaction:
                success = SUCCESS_RESPONSES['create_success'].format('Transaction')
                return AddTransaction(success=success, transaction=transaction)
        except Exception as e:
            raise GraphQLError(e)
