from Shop import *
from Product import *
from ThisThatQuestion import *
from MultipleChoiceQuestion import *
from Player import *
import sys
import time


def print_sl(text):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
        text = text[1:]
    print("\n")


def print_sl2(text):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
        text = text[1:]
    print("\n")


class Game:

    def play(self):
        ###############################################################
        #                   CREATING SHOP                             #
        ###############################################################
        shop = Shop()
        shop.add_products()
        ###############################################################
        #         ADDING QUESTIONS                                    #
        ###############################################################
        question1 = Question("Do bengal woods exist in poland? ", "no", 5)
        question2 = ThisThatQuestion("Is there a difference between an interface and an abstract class?",
                                     "yes", "no", 0, 10, 5)
        question3 = ThisThatQuestion("Is there a maximum to the amount of constructors a class can have in Java?",
                                     "yes", "no", 1, 20, 4)
        question4 = MultipleChoiceQuestion("What is the best achievable complexity of in situ sorting?",
                                           "O(N^2)", "O(N log N)", "O(N)", "O(log N)", "2", 10)
        question5 = Question("Are you over 18?", "yes", 10)
        question6 = ThisThatQuestion("Which of your hand is better than the other one?",
                                     "right", "left", "right", 20, 3)
        question7 = MultipleChoiceQuestion("Which color is the skies?", "red", "blue", "black", "white", 2, 5)

        questions = [question1, question2, question3, question4, question5, question6, question7]

        ###############################################################
        #                   PLAYER CREATION/START                     #
        ###############################################################
        print_sl("Creating a shop [--------------------]")
        print_sl("Creating products [--------------------]")
        print_sl("Creating a player. What is you name?")
        user_name = input("Write your username: ")
        player = Player(user_name)

        # Start
        print_sl("Welcome to the game 'BUY ME' {}".format(user_name))
        print_sl("THE RULES ARE PRESENTED HERE, PLEASE READ THEM CAREFULLY:")
        print_sl2("You have to earn money by answering the questions")
        print_sl2("Okay... answer to some of the questions and get the most of money you can")
        print_sl2("You will escape game when input will not face requirements (try 'break' while asked for input)")

        ###############################################################
        #                   ASKING QUESTIONS                          #
        ###############################################################
        answer1 = input(question1)
        if question1.correct_check(answer1):
            player.money += question1.money_prize
            print("Good answer. Your money: {}".format(player.money))
        answer2 = input(question2)
        if question2.correct_check(answer2):
            player.money += question2.money_prize + question2.bonus
            print("Good answer. Your money: {}".format(player.money))
        answer3 = input(question3)
        if question3.correct_check(answer3):
            player.money += question3.money_prize + question3.bonus
            print("Good answer. Your money: {}".format(player.money))
        answer4 = input(question4)
        if question4.correct_check(answer4):
            player.money += question3.money_prize
            print("Good answer. Your money: {}".format(player.money))
        answer5 = input(question5)
        if question5.correct_check(answer5):
            player.money += question5.money_prize
            print("Good answer. Your money: {}".format(player.money))

        ###############################################################
        #                   GAME LOOP                                 #
        ###############################################################
        print("\n\n\n")
        print_sl2("Part for some more enjoyable time!")
        print_sl("Remember that you can always escape by entering non-int character")

        playing = True
        index = 0
        while playing:
            try:
                print("#" * 20)
                print("AVAILABLE PRODUCTS")
                print("#" * 20)
                shop.list_all_products()
                print("Products in the bag: {}".format(player.bag))
                money = player.money
                price = shop.get_price(index)
                rest_money = money - price
                print("Available money: {}".format(rest_money))
                product_number = int(input("\nChoose what do you want to buy (number): \n"))
                print(player.add_to_bag(product_number))
                index += 1
                shop.remove_item(product_number - 1)
            except:
                print("Thank you for participation")
                playing = False
