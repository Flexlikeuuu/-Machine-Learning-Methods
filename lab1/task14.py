class BankAccount:
    interest_rate = 0.05
    total_accounts = 0

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner}: баланс пополнен на {amount}. Текущий баланс: {self.balance}")

    def withdraw(self, amount: float):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner}: снято {amount}. Текущий баланс: {self.balance}")

    @classmethod
    def set_interest_rate(cls, new_rate: float):
        cls.interest_rate = new_rate
        print(f"Процентная ставка изменена на {new_rate * 100}%")

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        return amount > 0


if __name__ == "__main__":
    acc1 = BankAccount("Иван", 1000)
    acc2 = BankAccount("Анна", 2500)

    acc1.deposit(500)
    acc1.withdraw(200)

    print(f"Валидность суммы 150: {BankAccount.is_valid_amount(150)}")
    print(f"Валидность суммы -50: {BankAccount.is_valid_amount(-50)}")

    BankAccount.set_interest_rate(0.07)
    print(f"Всего создано счетов: {BankAccount.get_total_accounts()}")