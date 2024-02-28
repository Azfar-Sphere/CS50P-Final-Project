class Stock():

    money_ = 10000

    def __init__(self, name: str):
        self._name = name
        self._quantity = 0

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def quantity(self) -> int:
        return self._quantity

    def buy(self, quantity: int):
        self._quantity += quantity

    def sell(self, quantity: int):
        self._quantity -= quantity

    def price(self) -> int:
        self._name
    
    def __str__(self) -> str:
        return f"{self._name}, Quantity: {self._quantity}"

    @classmethod
    def money(cls) -> int:
        return cls.money_

def main():
    AAPL = Stock("AAPL")
    AAPL.buy(10)
    print(AAPL)
    print(Stock.money())

if __name__ == "__main__":
    main()