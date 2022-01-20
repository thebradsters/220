"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area=", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume=", volume)

def shooting_percentage():
    shots = eval(input("Enter the player's total shots: "))
    made = eval(input("Enter how many shots the player made: "))
    percentage = made / shots * 100
    print("Shooting Percentage: ", percentage)

def coffee():
    pounds = eval(input("How many pounds of coffee would you like? "))
    drink = pounds * 10.50
    shipping = pounds * 0.86
    total = drink + shipping + 1.50
    print("You're total is: ", total)

def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel? "))
    miles = kilometers * 0.62137
    print("That's", miles, "miles!")


if __name__ == '__main__':
    pass
