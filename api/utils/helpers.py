from django.contrib.auth.models import update_last_login
from graphql_jwt.utils import jwt_encode, jwt_payload
from functools import wraps
from graphql import GraphQLError
from graphql.type import GraphQLResolveInfo as ResolveInfo
from django.utils.translation import gettext as _
from api.utils.common_responses import ERROR_RESPONSES


def super_user_permission():
    """
    Check if a user is an admin.
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            info = [arg for arg in args if isinstance(arg, ResolveInfo)]

            user = info[0].context.user
            if user.is_admin:
                return f(*args, **kwargs)
            raise GraphQLError(
                _(ERROR_RESPONSES["permission_denied"])
            )

        return wrapper
    return decorator


def check_authorization(app, action, model):
    """
    Check user's permission based on their role

    Args:
        app: django app name
        action: model action such as (add, change, delete, view)
        model: database model in lowercase
    """

    allowed_app = app  # django app name
    allowed_action = action  # action (add, change, delete, view)
    allowed_model = model  # the model name in lowercase letters

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            info = [arg for arg in args if isinstance(arg, ResolveInfo)]

            user = info[0].context.user

            if user.has_perm('{}.{}_{}'.format(
                    allowed_app,
                    allowed_action,
                    allowed_model)):
                return f(*args, **kwargs)
            raise GraphQLError(
                _(ERROR_RESPONSES["permission_denied"])
            )
        return wrapper
    return decorator


def generate_tokens(user):
    """
    generate tokens
    Args:
        user(Object): user's object from the database
    Returns:
        token, rest_token(tuple)
    """
    update_last_login(sender=None, user=user)

    # token to access GraphQL-based views
    payload = jwt_payload(user)
    token = jwt_encode(payload)

    return token


