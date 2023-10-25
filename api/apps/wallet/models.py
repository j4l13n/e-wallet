from django.db import models

from api.models import BaseModel
from api.apps.authenticate.models import User


# Wallet Model
class Wallet(BaseModel):
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer_wallet")  # Establishing a one-to-many relationship

    def __str__(self):
        return f"Wallet for {self.customer}"

# Transaction Model
class Transaction(BaseModel):
    AMOUNT_CHOICES = (
        ("credit", "Credit"),
        ("debit", "Debit"),
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=AMOUNT_CHOICES)
    source_wallet = models.ForeignKey(Wallet, related_name='transactions_as_source', on_delete=models.CASCADE)
    destination_wallet = models.ForeignKey(Wallet, related_name='transactions_as_destination', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id}"
