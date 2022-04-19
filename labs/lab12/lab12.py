import algorithms
from random import randint


def find_and_remove_first(my_list, value):
    i = 0
    while i < len(my_list):
        if my_list[i] == value:
            my_list.pop(i)
            my_list.insert(i, "brad")
            i = len(my_list)
        else:
            i += 1


def good_input():
    user_input = eval(input("enter a number 1 - 10: "))
    while user_input > 10 or user_input < 1:
        print("bad input, did you enter a number 1 - 10? ")
        user_input = eval(input("enter a number 1 - 10: "))
    print("good input")


def num_digits():
    user_input = eval(input("enter a positive number <<negative to close>>: "))
    while user_input > 0:
        count = 0
        while user_input > 0:
            user_input = user_input // 10
            count += 1
        print("there are {} digits in the number".format(count))
        user_input = eval(input("enter a positive number <<negative to close>>: "))


def hi_lo_game():
    guesses = 7
    tries = 0
    random_number = randint(1, 100)
    while tries != guesses:
        user_input = eval(input("guess a number 1 - 100: "))
        if user_input < random_number:
            print("too low")
            tries += 1
        if user_input > random_number:
            print("too high")
            tries += 1
        if user_input == random_number:
            print("correct")
            tries = 7


if __name__ == "__main__":
    my_list = [1, "dog", 44, "cat", 92]
    value = 92
    find_and_remove_first(my_list, value)
    print(my_list)

    good_input()
    num_digits()
    hi_lo_game()