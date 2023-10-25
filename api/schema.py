import graphene
import graphql_jwt
from graphene_django.debug import DjangoDebug

from api.apps.authenticate.schema.mutations import Mutation as AuthMutation


class Query(graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')
    pass


class Mutation(AuthMutation):
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
