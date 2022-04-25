from graphics import *
from random import randint


def read_data(filename):
    in_file = open(filename, 'r')
    big_list = in_file.read().replace('\n', ' ').split()
    my_list = []
    i = 0
    while i < len(big_list):
        my_list.append(eval(big_list[i]))
        i += 1
    return my_list


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val == values[i]:
            return True
        i += 1
    return False
