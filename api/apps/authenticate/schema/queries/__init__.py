import graphene
from graphene_django_extras import DjangoFilterPaginateListField, DjangoObjectField, LimitOffsetGraphqlPagination

from api.apps.authenticate.schema.types.user import UserType, UserListType


class Queries(graphene.ObjectType):
    users = DjangoFilterPaginateListField(UserType, pagination=LimitOffsetGraphqlPagination())
    user = DjangoObjectField(UserType, description='Single User query')
