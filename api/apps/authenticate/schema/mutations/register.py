import graphene
from graphql_jwt.decorators import login_required
from graphql import GraphQLError
from api.apps.authenticate.schema.types.user import UserInputType, UserType
from api.apps.authenticate.models import User
from api.utils.database import SaveContextManager, get_model_object
from api.utils.validators import validator
from rest_framework.authtoken.models import Token
from api.utils.helpers import generate_tokens
from api.utils.common_responses import SUCCESS_RESPONSES


class Register(graphene.Mutation):
    """
    Registration Mutation

    Args:
        new_user ([obj]): [user data object]
    """
    success = graphene.String()
    user = graphene.Field(UserType)
    token = graphene.String()
    rest_token = graphene.String()

    class Arguments:
        mobile = graphene.String()
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        mobile = kwargs.get('mobile')
        email = validator.is_email(kwargs.get('email'))
        password = validator.is_valid_password( kwargs.get('password'))

        user_instance = User(
            mobile=mobile,
            email=email
        )
        user_instance.is_active = True

        
        user_instance.set_password(password)

        with SaveContextManager(user_instance, model=User) as user:
            message = SUCCESS_RESPONSES["login_success"]
            token = generate_tokens(user)
            rest_payload = Token.objects.get_or_create(user=user)
            rest_token = rest_payload[0]
            return Register(success=SUCCESS_RESPONSES['register_success'], user=user, token=token, rest_token=rest_token)
