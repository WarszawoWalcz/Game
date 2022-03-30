class Product:
    def __init__(self, name, price, space, quantity):
        self.name = name
        self.price = price
        self.space = space
        self.quantity = quantity

    def __str__(self):
        return "{} - price: {} quantity: {}".format(self.name, self.price, self.quantity)
