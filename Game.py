import random

from Shop import *
from ThisThatQuestion import *
from MultipleChoiceQuestion import *
from Player import *
import sys
import time


def print_sl(text):
    """
    Writes The command line text slower and in suitable, game-style way.
    :param text:
    """
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
        text = text[1:]
    print("\n")


def print_sl2(text):
    """
    Writes the command line text slower and in suitable way faster than print_sl
    :param text:
    """
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
        text = text[1:]
    print("\n")


class Game:

    def __init__(self):
        self.questions = []

    def play(self):
        """
        Runs the whole game and keeps track of logics and UI
        """
        ###########################################
        #             CREATING SHOP               #
        ###########################################
        global product_number
        shop = Shop()
        ###############################
        #       ADDING QUESTIONS      #
        ###############################
        question1 = Question("Do bengal woods exist in poland? ", "no", 5)
        question2 = ThisThatQuestion("Is there a difference between an interface and an abstract class?",
                                     "yes", "no", "yes", 10, 5)
        question3 = ThisThatQuestion("Is there a maximum to the amount of constructors a class can have in Java?",
                                     "yes", "no", "no", 20, 4)
        question4 = MultipleChoiceQuestion("What is the best achievable complexity of in situ sorting?",
                                           "O(N^2)", "O(N log N)", "O(N)", "O(log N)", "2", 10)
        question5 = Question("Are you over 18?", "yes", 10)
        question6 = ThisThatQuestion("Which of your hand is better than the other one?",
                                     "right", "left", "right", 20, 3)
        question7 = MultipleChoiceQuestion("Which color is the skies?", "red", "blue", "black", "white", "blue", 5)

        self.questions = [question1, question2, question3,
                          question4, question5, question6,
                          question7]

        #####################################
        #        PLAYER CREATION/START     #
        ####################################
        print_sl("Creating a shop [--------------------]")
        print_sl("Creating products [--------------------]")
        print_sl("Creating a player. What is you name?")
        user_name = input("Write your username: ")
        player = Player(user_name, 3)

        # Start
        print_sl("Welcome {} to the game 'STEAL ME'".format(user_name))
        print_sl2("[-----------------------------------------------------]")
        print_sl("THE RULES ARE PRESENTED HERE, PLEASE READ THEM CAREFULLY:")
        print_sl2("[----------------------------------------------------------------]")
        print_sl2("You steal products to survive on the street, but do NOT GET CAUGHT")
        print_sl2("[------------------------------------------------------------------------]")
        print_sl2("Write just a number for example '1' to get product from a list. Try now")
        print_sl2("[----------------------------------------------------------------------]")
        print_sl2("EXPLANATIONS:")
        print_sl(" - You need to earn euros by answering questions and receiving bonus.")

        ################################
        #           GAME LOOP         #
        ###############################
        player.money = 10
        print_sl2("You get 10 euro for free. Enjoy")
        playing = True
        round_index = 1
        while playing and player.lives > 0 and player.money > 0:
            print("#" * 20)
            print("AVAILABLE PRODUCTS")
            print("#" * 20)
            shop.list_all_products()
            print_sl2("---------------------------------------------")
            print("Products in robbery jacket: {}".format(player.bag))
            print("Your money: {} euro".format(player.money))
            print_sl2("What do you want to steal {}? Take a look\n".format(player.name))
            try:
                product_number = int(input("Write number corresponding to the product: "))
                assert product_number > 0, "Number should be positive"
            except ValueError:
                print("Please write number instead of name etc.")
                print_sl2("----------- R E S E T  G A M E -----------")
                self.play()
            print_sl2("--------------------------------------------------------")
            print_sl("Okay, if you want to get that you need to answer question")
            print_sl2("--------------------------------------------------------")

            question = self.questions[0]
            answer = input(question)
            self.questions.pop(0)
            if question.correct_check(answer):
                if player.money > 0:
                    player.add_to_bag(shop.products_list[product_number-1].name)
                    shop.remove_item(product_number - 1)
                    player.money += shop.products_list[product_number-1].price
                if isinstance(question, ThisThatQuestion):
                    player.money += question.bonus
                print("Good answer")
            else:
                print("You loose one of {} lives!".format(player.lives))
                player.lives -= 1
            if round_index % 5 == 0:
                random_boss_price = random.randint(1, 10)
                print_sl2("Your boss wants some money from you! Give him {} euro or you will die!".format(random_boss_price))
                print_sl2("Proceeding to take money from your wallet")
                player.money -= random_boss_price
            print_sl("Taking daily 1 euro loss")
            player.money -= 1
            print_sl("Earning money for the products. Money: ".format(player.money))
            print_sl("-------------------------")

            continue_asking = True
            while continue_asking:
                if_continue = input("Do you want to continue? Press [y/n]")
                if if_continue == 'n':
                    playing = False
                    continue_asking = False
                elif if_continue == 'y':
                    continue_asking = False
            round_index += 1
