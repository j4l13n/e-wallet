import graphene
from graphene_django_extras import DjangoListObjectField, DjangoFilterListField, DjangoFilterPaginateListField, DjangoObjectField

from api.apps.wallet.schema.types import WalletListType, TransactionListType, WalletType, TransactionType


class Queries(graphene.ObjectType):
    wallets = DjangoListObjectField(
        WalletListType, description=" Paginated Wallet's List ")
    transactions = DjangoListObjectField(
        TransactionListType, description=" Paginated Transactions's List ")
    wallet = DjangoObjectField(WalletType, description='Single Wallet query')
    transaction = DjangoObjectField(
        TransactionType, description='Single Transaction query')
