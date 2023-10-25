import graphene
from graphql import GraphQLError
from graphql_jwt.decorators import login_required
from django.contrib.auth.hashers import check_password
from ...models import User
from .....utils.app_utils.database import get_model_object
from .....utils.app_utils.validators import validator
from api.utils.common_responses import ERROR_RESPONSES, SUCCESS_RESPONSES


class ChangePassword(graphene.Mutation):
    """
    Change Password Mutation

    Args:
        id (str): user primary key
        current_password (str): current password
        new_password (str): new password
    """
    success = graphene.String()

    class Arguments:
        id = graphene.String(required=True)
        current_password = graphene.String()
        new_password = graphene.String()

    @login_required
    def mutate(self, info, **kwargs):
        user = get_model_object(User, 'id', kwargs.get('id'))

        if not check_password(kwargs.get('current_password'), user.password):
            raise GraphQLError(ERROR_RESPONSES['not_a_match'])

        if check_password(kwargs.get('new_password'), user.password):
            raise GraphQLError(ERROR_RESPONSES['similar_password'])

        new_password = validator.is_valid_password(kwargs.get('new_password'))

        if new_password:
            user.set_password(new_password)
            user.save()

        success = SUCCESS_RESPONSES['password_changed'].format(
            user.email)

        return ChangePassword(success=success)
