# Using the Wallet and Transaction API

This tutorial will guide you through using the API to manage wallets and transactions in the "Tekana-eWallet" application.

## Prerequisites

Before you get started, make sure you have the necessary tools and permissions:

- A running instance of the "Tekana-eWallet" application.
- Access to the API endpoints.
- A tool for making HTTP requests, such as `curl` or a GUI tool like Postman.

## Wallets

### Querying Wallets

To retrieve wallet information, use the following query:

```graphql
query {
    wallets {
        id
        balance
        customer {
        id
        username
        email
        }
    }
}
```
- Replace id, balance, and customer with the fields you want to retrieve.
- Execute the query using your preferred HTTP client, providing the appropriate URL for your API endpoint.

### Creating a Wallet

To create a new wallet, use the following mutation:

```graphql
mutation {
  createWallet(input: {
    balance: 100.00
    customer: 1  # Replace with the customer's ID
  }) {
    wallet {
      id
      balance
    }
  }
}
```
- Replace balance with the initial balance of the wallet.
- Replace customer with the ID of the customer who owns the wallet.
- Execute the mutation using your preferred HTTP client.

## Transactions

### Querying Transactions

To retrieve transaction history, use the following query:

```graphql
query {
  transactions {
    id
    amount
    transactionType
    sourceWallet {
      id
      balance
    }
    destinationWallet {
      id
      balance
    }
    timestamp
  }
}
```
- Replace id, amount, transactionType, sourceWallet, destinationWallet, and timestamp with the fields you want to retrieve.
- Execute the query using your preferred HTTP client.


### Creating a Transaction

To create a new transaction, use the following mutation:

```graphql
mutation {
  createTransaction(input: {
    amount: 50.00
    transactionType: "debit"  # or "credit"
    sourceWallet: 1  # Replace with the source wallet's ID
    destinationWallet: 2  # Replace with the destination wallet's ID
  }) {
    transaction {
      id
      amount
    }
  }
}
```
- Replace amount with the transaction amount.
- Choose transactionType as either "debit" or "credit."
- Replace sourceWallet with the ID of the source wallet.
- Replace destinationWallet with the ID of the destination wallet.
- Execute the mutation using your preferred HTTP client.


## Conclusion

You've now learned how to use the API to manage wallets and transactions in the "Tekana-eWallet" application. Customize your queries and mutations based on your requirements.

If you encounter any issues or have questions, please refer to the project documentation or contact our support team.