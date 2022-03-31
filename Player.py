class Player:
    money = 0
    bag = []

    def __init__(self, name, num_lives):
        self.name = name
        self.lives = num_lives

    def add_to_bag(self, product):
        """
        Adds given product to the players bag
        :param product:
        """
        self.bag.append(product)
