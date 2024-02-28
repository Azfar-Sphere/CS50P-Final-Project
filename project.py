class Stock():

    money = 10000

    def __init__(self, name: str, quantity: int)
        self._name = name
        self._quantity = quantity
    
    @property
    def stock_name(self):
        return self._name
    
    @stock_name.setter
    def change_stock(self, type: str):
        if type.lower() != "buy" and type != "sell":
            print("Error, expected buy or sell as argument")





def main():


if __name__ == "__main__":
    main()