from django.test import TestCase
from graphene.test import Client
import jwt
from django.conf import settings
from datetime import datetime, timedelta

from api.schema import schema


class AuthenticateTestCase(TestCase):
    def setUp(self):
        self.client = Client(schema)


    def test_register_mutation(self):
        # Define Test Data
        user_data = {
            "mobile": "0784489000",
            "email": "test@gmail.com",
            "password": "Test123Test123"
        }

        # Define the mutation
        mutation = """
        mutation {
            register(
                mobile: "%s"
                email: "%s"
                password: "%s"
            ) {
                success
                token
                restToken
                user {
                    id
                    email
                }
            }
        }
        """ % (user_data['mobile'], user_data['email'], user_data['password'])

        # Execute the mutation
        executed = self.client.execute(mutation)

        # Assert to check the response data
        self.assertEqual(executed['data']["register"]["success"], "You have successfully registered!")
        self.assertEqual(executed['data']["register"]["user"]["email"], user_data['email'])
        self.assertIn('token', executed['data']["register"])
        self.assertIn('restToken', executed['data']["register"])



