"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math

def cash_converter():
    integer = float(input("enter an integer: "))
    print("That is ${}0".format(integer))


def encode():
    message = input("enter a message: ")
    key = int(input("enter a key: "))
    length = len(message)
    my_string = ""
    for i in range(length):
        letter = message[i]
        encoded = ord(letter) + key
        decoded = chr(encoded)
        my_string = my_string + decoded
    print(my_string)


def sphere_area(radius):
    area = 4 * math.pi * (radius ** 2)
    return area


def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume


def sum_n(number):
    num_sum = 0
    for num in range(1, number + 1):
        num_sum = num_sum + num
    return num_sum


def sum_n_cubes(number):
    num_sum = 0
    for num in range(1, number + 1):
        num_sum = num_sum + (num ** 3)
    return num_sum


def encode_better():
    message = input("enter a message: ")
    key = input("enter a key: ")
    length = len(message)
    key_length = len(key)
    my_string = ""
    for i in range(length):
        letter = message[i]
        number_key = i % key_length
        letter_key = key[number_key]
        encoded = ord(letter) - 65
        key_encoded = ord(letter_key) - 65
        both_encoded = encoded + key_encoded
        encode_mod = (both_encoded % 58) + 65
        decoded = chr(encode_mod)
        my_string = my_string + decoded
    print(my_string)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
