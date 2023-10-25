from django.db import models

# Customer (User) Model
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # You may want to use a password hashing library

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Wallet Model
class Wallet(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Establishing a one-to-many relationship

    def __str__(self):
        return f"Wallet for {self.customer}"

# Transaction Model
class Transaction(models.Model):
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
