class InsufficientFundsError(Exception):
    """Raised when an account does not have enough balance for a withdrawal or transfer."""


class Account:
    def __init__(self, account_id: str, balance: float = 0.0):
        self.account_id = account_id
        self.balance = float(balance)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Account {self.account_id} has insufficient funds: requested {amount}, available {self.balance}"
            )
        self.balance -= amount


def depositAcc(account: Account, amount: float) -> None:
    """Deposit money into an account."""
    account.deposit(amount)


def withdrawAcc(account: Account, amount: float) -> None:
    """Withdraw money from an account, raising InsufficientFundsError if funds are insufficient."""
    account.withdraw(amount)


def transfer(source: Account, destination: Account, amount: float) -> None:
    """Transfer funds from one account to another."""
    if amount <= 0:
        raise ValueError("Transfer amount must be positive")
    source.withdraw(amount)
    destination.deposit(amount)


def main() -> None:
    checking = Account("CHK-1001", 500.0)
    savings = Account("SVG-2002", 250.0)

    print(f"Initial balances: checking={checking.balance}, savings={savings.balance}")

    depositAcc(checking, 150.0)
    print(f"After deposit: checking={checking.balance}")

    try:
        withdrawAcc(savings, 300.0)
    except InsufficientFundsError as exc:
        print(f"Withdrawal failed: {exc}")

    transfer(checking, savings, 200.0)
    print(f"After transfer: checking={checking.balance}, savings={savings.balance}")


if __name__ == "__main__":
    main()
