# Tekana-eWallet GraphQL API Reference

The Tekana-eWallet GraphQL API allows you to manage wallets and transactions in the application. This reference provides an overview of the available queries and mutations.

## Wallets

### Querying Wallets

- **Description:** Retrieve a list of wallets along with their details.
- **Query:**

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

### Creating a Wallet

- **Description**: Create a new wallet for a customer.
- **Mutation**:
```graphql
mutation {
  createWallet(input: {
    balance: Float!
    customer: ID!
  }) {
    wallet {
      id
      balance
    }
  }
}
```
- `balance`: The initial balance of the wallet.
- `customer`: The ID of the customer who owns the wallet.


## Transactions


### Querying Transactions

- **Description**: Retrieve a list of transactions along with their details.
- **Query**:

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

### Creating a Transaction

- **Description**: Create a new transaction.
- **Mutation**:
```graphql
mutation {
  createTransaction(input: {
    amount: Float!
    transactionType: "credit" or "debit"
    sourceWallet: ID!
    destinationWallet: ID!
  }) {
    transaction {
      id
      amount
    }
  }
}
```

- `amount`: The transaction amount.
- `transactionType`: The type of transaction, either "credit" or "debit."
- `sourceWallet`: The ID of the source wallet.
- `destinationWallet`: The ID of the destination wallet.


## Conclusion

This reference documentation provides an overview of the available GraphQL queries and mutations for managing wallets and transactions in the Tekana-eWallet application. Use this reference to interact with the API and customize queries and mutations as needed for your project.