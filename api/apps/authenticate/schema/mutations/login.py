import graphene
from graphql import GraphQLError
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
from rest_framework.authtoken.models import Token

from api.apps.authenticate.schema.types.user import UserType
from api.apps.authenticate.models import User
from api.utils.common_responses import \
    SUCCESS_RESPONSES, ERROR_RESPONSES
from api.utils.helpers import generate_tokens


class Login(graphene.Mutation):
    """
    Login a user with their credentials
    args:
        password(str): user's password
        email(str): user's email
    returns:
        message(str): success message confirming login
        token(str): JWT authorization token used to validate the login
        rest_token(str): JWT token used to validate REST endpoint access
        user(obj): 'User' object containing details of the logged in user
    """
    success = graphene.String()
    token = graphene.String()
    rest_token = graphene.String()
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')
        message = ERROR_RESPONSES["invalid_credentials"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise GraphQLError(_(ERROR_RESPONSES["invalid_credentials"]))

        if user.is_active:
            user_auth = authenticate(username=email, password=password)

            if not user_auth:
                raise GraphQLError(_(message))

            message = SUCCESS_RESPONSES["login_success"]

            token = generate_tokens(user_auth)

            rest_payload = Token.objects.get_or_create(user=user_auth)
            rest_token = rest_payload[0]

            return Login(success=_(message), rest_token=rest_token, token=token, user=user_auth)

        return GraphQLError(_(ERROR_RESPONSES["not_active"]))
