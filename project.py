class Stock():

    money = 10000

    def __init__(self, name: str, quantity: int):
        self._name = name
        self._quantity = 0
        self.quantity("buy", quantity)

    @property
    def name(self):
        return self._name
    
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, type: str, quantity: int):
        type = type.lower()

        if type != "buy" and type != "sell":
            print("Error, expected buy or sell")

        if type == "buy":
            self._quantity += quantity

    def __str__(self):
        return f"{self._name}, Quantity: {self._quantity}"



def main():
    APPL = Stock("APPL", 10)
    print(APPL)
if __name__ == "__main__":
    main()