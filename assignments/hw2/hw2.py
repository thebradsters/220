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


def sum_of_threes():
    upper = eval(input("what is the upper bound? "))
    sum = 0
    for i in range(sum, upper + 1, 3):
        sum = sum + i
    print("sum of threes is", sum)

def multiplication_table():
    pass



def triangle_area():
    a = eval(input("Enter side a length: "))
    b = eval(input("Enter side b length: "))
    c = eval(input("Enter side c length: "))
    area = (a + b + c) / 2
    print("area is", area)

def sum_squares():
    lower = eval(input("Enter lower range: "))
    upper = eval(input("Enter upper range: "))
    sum = 0
    for i in range(sum, upper + 1):
        sum = sum + (i * i)
    print(sum)

def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))
    power = 1
    for i in range(power, exponent + 1):
        power = power * base
    print(base, "^", exponent, "=", power)


if __name__ == '__main__':
    pass
