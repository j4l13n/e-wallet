from django.test import TestCase
from graphene.test import Client
import jwt
from django.conf import settings
from datetime import datetime, timedelta
from django.test import TestCase
from graphene.test import Client
from api.apps.wallet.models import Transaction
from api.apps.wallet.schema.types import TransactionType, TransactionInputType
from api.apps.wallet.schema.mutations import AddTransaction
from api.apps.wallet.serializers import TransactionSerializer

from api.schema import schema


class TransactionTestCase(TestCase):
    def setUp(self):
        self.client = Client(schema)

    def test_add_transaction_with_unknown_wallet_mutation(self):
        new_transaction_data = {
            'amount': 100.0,
            'transactionType': 'DEBIT',
            'sourceWallet': "erlnmsogf",
            'destinationWallet': "b7ag9mqcd",
        }
        response = self.client.execute('''
            mutation AddTransaction($newTransaction: TransactionInputType!) {
                addTransaction(newTransaction: $newTransaction) {
                    success
                    transaction {
                        id
                        amount
                    }
                }
            }
        ''', variables={'newTransaction': new_transaction_data})

        # Check the error response
        error = response['errors'][0]
        self.assertEqual(error['message'], 'Wallet with id erlnmsogf does not exist.')
