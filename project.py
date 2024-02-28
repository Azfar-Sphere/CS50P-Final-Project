class Stock():

    money = 10000

    def __init__(self, name: str):
        self._name = name
        self._quantity = 0

    @property
    def name(self):
        return self._name
    
    @property
    def quantity(self):
        return self._quantity

    def buy(self, quantity: int):
        self._quantity += quantity

    def sell(self, quantity: int):
        self._quantity -= quantity

    def price(self):
        self._name
    
    def __str__(self):
        return f"{self._name}, Quantity: {self._quantity}"



def main():
    AAPL = Stock("AAPL")
    AAPL.buy(10)
    print(AAPL)
if __name__ == "__main__":
    main()