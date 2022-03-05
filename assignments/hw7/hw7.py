"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import encryption


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    message = in_file.read()
    new_message = message.replace("\n", " ")
    splat = new_message.split()
    length = len(splat)
    for i in range(length):
        words = i + 1
        new = splat[i]
        print(words, new, file=out_file)


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    for line in in_file.readlines():
        splat = line.split()
        math_1 = float(splat[2]) + 1.65
        paid_1 = math_1 * float(splat[3])
        formatted = "{0:.2f}".format(paid_1)
        str_list_1 = splat[0] + " " + splat[1]
        end_pay_1 = str_list_1 + " " + str(formatted)
        print(end_pay_1, file=out_file)


def calc_check_sum(isbn):
    isbn = isbn.replace("-", "")
    total = 0
    for i in range(10):
        total = total + int(isbn[i]) * (10 - i)
    return total


def send_message(file_name, friend_name):
    first = open(file_name, 'r')
    read = first.read()
    strip = read.rstrip()
    friend_file = friend_name + '.txt'
    file = open(friend_file, 'w')
    print(strip, file=file)


def encode(message, key):
    length = len(message)
    my_string = ""
    for i in range(length):
        letter = message[i]
        encoded = ord(letter) + key
        decoded = chr(encoded)
        my_string = my_string + decoded
    return my_string


def send_safe_message(file_name, friend_name, key):
    first = open(file_name, 'r')
    read = first.read()
    friend_file = friend_name + '.txt'
    file = open(friend_file, 'w')
    words = ""
    for line in read:
        encrypt = encryption.encode(line, key)
        words = words + encrypt
        print(words, file=file)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass


if __name__ == '__main__':
    pass
