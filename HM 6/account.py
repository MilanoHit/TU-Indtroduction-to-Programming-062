from Errorrs import InvalidAccountType
from Errorrs import InvalidAccountData

class Account:
    ACC_TYPES = ("SAVINGS", "CREDIT", "PAYMENT")

    def __init__(self, iban, currency, type1) -> None:
        if type1 not in self.ACC_TYPES:
            raise InvalidAccountType()

        try:
            currency = int(currency)
        except:
            raise InvalidAccountData()

        self.iban = iban
        self.currency = currency
        self.type = type1

    def print(self):
        print(f"{self.iban}: {self.currency}, {self.type}")

    def deposit(self, currency):
        try:
            currency = int(currency)
        except:
            raise InvalidAccountData()

        self.currency += currency

    def withdraw(self, currency):
        try:
            currency = int(currency)
        except:
            raise InvalidAccountData()

        self.currency -= currency