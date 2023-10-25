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

    def test_add_transaction_mutation(self):
        new_transaction_data = {
            'amount': 100.0,
            'transactionType': 'DEBIT',
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
        import pdb; pdb.set_trace()

        # Ensure the mutation executed successfully
        self.assertIsNone(response.errors)

        # Check the response data for the success message and the created transaction
        data = response.data['addTransaction']
        self.assertEqual(data['success'], 'Transaction created successfully')
        transaction_data = data['transaction']
        self.assertEqual(transaction_data['amount'], new_transaction_data['amount'])

        # Check that a Transaction instance was created in the database
        transaction_id = transaction_data['id']
        self.assertTrue(Transaction.objects.filter(id=transaction_id).exists())

    def test_add_transaction_mutation_with_invalid_data(self):
        # Test the mutation with invalid data to check if it raises an error
        invalid_transaction_data = {
            'amount': 'invalid_amount',  # Invalid data
            'description': 'Test transaction',
        }
        response = self.client.execute('''
            mutation AddTransaction($newTransaction: TransactionInputType!) {
                addTransaction(newTransaction: $newTransaction) {
                    success
                    transaction {
                        id
                    }
                }
            }
        ''', variables={'newTransaction': invalid_transaction_data})

        # Ensure the mutation returns an error
        # self.assertIsNotNone(response.errors)
        # self.assertEqual(response.errors[0].message, 'Invalid input.')

        # Ensure no Transaction instance was created in the database
        self.assertFalse(Transaction.objects.filter(description='Test transaction').exists())
