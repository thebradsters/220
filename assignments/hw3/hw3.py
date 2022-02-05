"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def average():
    var = eval(input("how many grades will you enter? "))
    sum = 0
    for i in range(1, var + 1):
        grades = eval(input("enter grade: "))
        sum = sum + grades
        norm = sum / var
    print("average is", norm)

def tip_jar():
    sum = 0
    for i in range(1, 5 + 1):
        var = eval(input("how much would you like to donate?"))
        sum = sum + var
    print("total tips:", sum)

def newton():
    var = eval(input("What number do you want to square root? "))
    improve = eval(input("How many times should we improve the approximation? "))
    sum = var
    for i in range(improve):
        i = i + 1
        sum = (sum + (var / sum )) / 2
    print("the square root is approximately", sum)

def sequence():
    terms = eval(input("how many terms would you like? "))
    for i in range(1, terms + 1):
        print((i - 1) + (i % 2), end=" ")

def pi():
    terms = eval(input("how many terms in the series? "))
    sum = 2
    for i in range(1, terms + 1):
        left = (2 * i) / (2 * i - 1)
        right = (2 * i) / (2 * i + 1)
        sum = sum * left * right
    print(sum)

if __name__ == '__main__':
    pass
