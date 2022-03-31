from Product import *


class Shop:
    def __init__(self):
        self.products_list = []
        self.products_list.append(
            Product("Coke", 2.50, 5, 2))
        self.products_list.append(
            Product("Sprite", 3, 5, 1))
        self.products_list.append(
            Product("Fanta", 3, 5, 2))
        self.products_list.append(
            Product("Lays", 1.50, 3, 1))
        self.products_list.append(
            Product("Cheetos", 5, 4, 3))
        self.products_list.append(
            Product("OCB", 5, 1, 1))
        self.products_list.append(
            Product("Arizona", 5, 7, 4))
        self.products_list.append(
            Product("Eggs", 5, 5, 2))
        self.products_list.append\
            (Product("Water", 5, 4, 2))
        self.products_list.append(
            Product("Chinese soup", 5, 7, 2))
        self.products_list.append(
            Product("Tea", 5, 3, 1))
        self.products_list.append(
            Product("Hot dog", 5, 7, 1))
        self.products_list.append(
            Product("Beer", 5, 5, 1))
        self.products_list.append\
            (Product("Skittles green", 5, 4, 2))
        self.products_list.append(
            Product("Skittles red", 5, 7, 1))
        self.products_list.append\
            (Product("Redbull", 5, 6, 1))
        self.products_list.append(
            Product("Coffee", 5, 7, 1))
        self.products_list.append(
            Product("Reeses", 5, 5, 1))
        self.products_list.append\
            (Product("Cookies", 5, 5, 2))
        self.products_list.append(
            Product("Burger", 5, 4, 3))

    def list_all_products(self):
        """
        Lists all products from the shop
        for the player to keep track of them
        :return:
        """
        product_list_forloop = self.products_list
        index = 0
        for product_x in product_list_forloop:
            index += 1
            print("{}. {}".format(index, product_x))

    def remove_item(self, index):   # index - 1
        """
        Removes item from the shop
        :param index:
        """
        if self.products_list[index].quantity == 1:
            del self.products_list[index]
        else:
            self.products_list[index].quantity -= 1

    def get_price(self, index):     # index - 1
        return self.products_list[index].price
