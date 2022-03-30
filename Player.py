class Player:
    money = 0
    bag = []

    def __init__(self, name):
        self.name = name

    def add_to_bag(self, product):
        self.bag.append(product)
