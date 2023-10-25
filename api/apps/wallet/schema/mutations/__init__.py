import graphene
from .transaction import AddTransaction, TransactionSerializerMutation
from .wallet import AddWallet, WalletSerializerMutation


class Mutation(graphene.ObjectType):
    # Transaction Mutations
    add_transaction = AddTransaction.Field()
    transaction_create = TransactionSerializerMutation.CreateField(deprecation_reason='Some one deprecation message')
    transaction_delete = TransactionSerializerMutation.DeleteField()
    transaction_update = TransactionSerializerMutation.UpdateField()

    # Wallet Mutations
    add_wallet = AddWallet.Field()
    wallet_create = WalletSerializerMutation.CreateField(deprecation_reason='Some one deprecation message')
    wallet_delete = WalletSerializerMutation.DeleteField()
    wallet_update = WalletSerializerMutation.UpdateField()
