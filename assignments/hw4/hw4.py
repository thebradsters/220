"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

from graphics import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to make a square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 0), Point(0, 50))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()

        shape = shape.clone()
        shape.draw(win)
        shape.move(change_x, change_y)

    inst_pt2 = Point(width / 2, height - 200)
    instructions2 = Text(inst_pt2, "Click again to close")
    instructions2.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)
    click = win.getMouse()
    x_1 = click.getX()
    y_1 = click.getY()
    click2 = win.getMouse()
    x_2 = click2.getX()
    y_2 = click2.getY()

    shape = Rectangle(click, click2)
    shape.setOutline("green")
    shape.setFill("green")
    shape = shape.clone()
    shape.draw(win)

    inst = Point(width / 2, height - 200)
    instructions = Text(inst, "Click again to close")
    instructions.draw(win)

    length = abs(click.x - click2.x)
    width = abs(click.y - click2.y)
    perimeter = (2 * length) + (2 * width)
    area = length * width

    perimeter_box = Point(width / 2, height - 100)
    perimeter_txt = Text(perimeter_box, "Perimeter:")
    perimeter_txt.draw(win)
    perimeter_eq_box = Point(width / 2, height - 75)
    perimeter_eq_txt = Text(perimeter_eq_box, perimeter)
    perimeter_eq_txt.draw(win)


    area_box = Point(width / 2, height - 50)
    area_txt = Text(area_box, "Area:")
    area_txt.draw(win)
    area_eq_box = Point(width / 2, height - 25)
    area_eq_txt = Text(area_eq_box, area)
    area_eq_txt.draw(win)

    win.getMouse()
    win.close()


def circle():
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)
    click = win.getMouse()
    x_1 = click.getX()
    y_1 = click.getY()
    click2 = win.getMouse()
    x_2 = click2.getX()
    y_2 = click2.getY()

    shape = Circle(click, click2)
    shape.setOutline("light blue")
    shape.setFill("light blue")
    shape = shape.clone()
    shape.draw(win)

    inst = Point(width / 2, height - 200)
    instructions = Text(inst, "Click again to close")
    instructions.draw(win)

    radius_box = Point(width / 2, - 50)
    box_txt = Text(radius_box, "Radius")
    box_txt.draw(win)
    radius_eq = ((click2.x - click.x) + (click2.y - click.y))**(1/2)
    radius_eq_box = Point(width / 2, - 25)
    radius_txt = Text(radius_eq_box, radius_eq)
    radius_txt.draw(win)

    win.getMouse()
    win.close()

def pi2():
    input = eval(input("enter the number of terms to sum: "))
    sum = 0
    total = 0
    multiplier = 4
    for i in range(1, input + 1):
        sequence = (i - 1) + (i % 2)
        sum = sum + sequence
        total = sum * multiplier

    print("pi approximation:", total)
    accuracy = total ** (1 / 2)
    print("accuracy: ", accuracy)


if __name__ == '__main__':
    pass
