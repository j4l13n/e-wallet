import graphene
from graphene_django_extras import DjangoListObjectType, \
    DjangoObjectType, LimitOffsetGraphqlPagination, \
    DjangoInputObjectType
from api.apps.wallet.models import Wallet, Transaction


class WalletType(DjangoObjectType):
    class Meta:
        model = Wallet
        description = " Wallet Object Type "
        filter_fields = {
            'id': ('exact', ),
            'customer__id': ('exact', ),
            'balance': ('lte', 'gte', 'gt', 'exact', )
        }

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset


class WalletInputType(DjangoInputObjectType):
    class Meta:
        model = Wallet
        description = " Wallet Input Object Type "


class WalletListType(DjangoListObjectType):
    class Meta:
        model = Wallet
        description = " Wallet List Object Type "


class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction
        description = " Transaction Object Type "
        filter_fields = {
            'id': ('exact', ),
            'destination_wallet__id': ('exact', ),
            'source_wallet__id': ('exact', ),
            'transaction_type': ('exact', 'icontains', 'istartswith', ),
            'amount': ('exact', 'lte', 'gte', ),
            'timestamp': ('exact', 'lte', 'gte', )
        }


class TransactionInputType(DjangoInputObjectType):
    class Meta:
        model = Transaction
        description = " Transaction Input Object Type "


class TransactionListType(DjangoListObjectType):
    class Meta:
        model = Transaction
        description = " Transaction List Object Type "