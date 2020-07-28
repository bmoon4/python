class Product:
    def __init__(self, price):
        self.__price = price

    @property  # pythonic code
    def price(self):
        return self.__price

    @price.setter  # pythonic code
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative")
        else:
            self.__price = value


product = Product(10)
print(product.price)
