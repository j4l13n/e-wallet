import graphene
import graphql_jwt
from graphene_django.debug import DjangoDebug

from api.apps.authenticate.schema.mutations import Mutation as AuthMutation
from api.apps.wallet.schema.queries.wallet_queries import Queries as WalletQueries
from api.apps.wallet.schema.mutations import Mutation as WalletMutations


class Query(WalletQueries, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')
    pass


class Mutation(AuthMutation, WalletMutations):
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
