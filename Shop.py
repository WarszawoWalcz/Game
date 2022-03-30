from Product import *


class Shop:
    def __init__(self):
        self.products_list = []

    def add_products(self):
        self.products_list.append(Product("Coke", 2.50, 5, 4))
        self.products_list.append(Product("Sprite", 3, 5, 4))
        self.products_list.append(Product("Fanta", 3, 5, 7))
        self.products_list.append(Product("Lays", 1.50, 3, 2))
        self.products_list.append(Product("Cheetos", 5, 4, 16))
        self.products_list.append(Product("OCB", 5, 1, 1))
        self.products_list.append(Product("Arizona", 5, 7, 3))
        self.products_list.append(Product("Eggs", 5, 5, 2))
        self.products_list.append(Product("Water", 5, 4, 10))
        self.products_list.append(Product("Chinese soup", 5, 7, 10))
        self.products_list.append(Product("Tea", 5, 3, 5))
        self.products_list.append(Product("Hot dog", 5, 7, 10))
        self.products_list.append(Product("Beer",5, 5, 8))
        self.products_list.append(Product("Skittles green", 5, 4, 10))
        self.products_list.append(Product("Skittles red", 5, 7, 10))
        self.products_list.append(Product("Redbull", 5, 6, 6))
        self.products_list.append(Product("Coffee", 5, 7, 10))
        self.products_list.append(Product("Reeses", 5, 5, 8))
        self.products_list.append(Product("Cookies", 5, 5, 6))
        self.products_list.append(Product("Burger", 5, 4, 10))

    def list_all_products(self):
        product_list_forloop = self.products_list
        index = 0
        for product_x in product_list_forloop:
            index += 1
            print("{}. {}".format(index, product_x))

    def remove_item(self, index):   # index - 1
        del self.products_list[index]

    def get_price(self, index):
        if index == 1:
            return 2.50
        elif index == 2:
            return 3
        elif index == 3:
            return 3
        elif index == 4:
            return 1.50
        else:
            return 5
