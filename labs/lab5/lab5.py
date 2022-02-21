import math
from graphics import *

def triangle():
    win_width = 400
    win_height = 400
    win = GraphWin("Triangle", win_width, win_height)
    click = win.getMouse()
    x1 = click.getX()
    y1 = click.getY()
    click2 = win.getMouse()
    x2 = click2.getX()
    y2 = click2.getY()
    click3 = win.getMouse()
    x3 = click3.getX()
    y3 = click3.getY()

    da = x2 - x1
    db = y2 - y1
    dc = x3 - x2
    dd = y3 - y2
    de = x3 - x1
    df = y3 - y1
    pre_a = (da ** 2) + (db ** 2)
    pre_b = (dc ** 2) + (dd ** 2)
    pre_c = (de ** 2) + (df ** 2)
    a = math.sqrt(pre_a)
    b = math.sqrt(pre_b)
    c = math.sqrt(pre_c)

    shape = Polygon(click, click2, click3)
    shape.setOutline("blue")
    shape.setFill("blue")
    shape = shape.clone()
    shape.draw(win)

    dx = x3 - x2 - x1
    dy = y3 - y2 - y1
    tri_length = math.sqrt((dx ** 2) + (dy ** 2))

    perimeter_box = Point(win_width / 2, win_height - 100)
    perimeter_txt = Text(perimeter_box, "Perimeter:")
    perimeter_txt.draw(win)
    perimeter_eq_box = Point(win_width / 2, win_height - 75)
    perimeter_eq_txt = Text(perimeter_eq_box, tri_length)
    perimeter_eq_txt.draw(win)

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    area_box = Point(win_width / 2, win_height - 50)
    area_txt = Text(area_box, "Area:")
    area_txt.draw(win)
    area_eq_box = Point(win_width / 2, win_height - 25)
    area_eq_txt = Text(area_eq_box, area)
    area_eq_txt.draw(win)

    inst = Point(win_width / 2, win_height - 200)
    instructions = Text(inst, "Click again to close")
    instructions.draw(win)

    win.getMouse()
    win.close()



def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_input = Entry(Point(win_width / 2 - 5, win_height / 2 + 40), 5)
    red_input.setText("0")
    red_input.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_input = red_input.clone()
    green_input.move(0, 30)
    green_input.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_input = green_input.clone()
    blue_input.move(0, 30)
    blue_input.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for color in range(5):
        red = eval(red_input.getText())
        green = eval(green_input.getText())
        blue = eval(blue_input.getText())
        rgb = color_rgb(red, green, blue)
        win.getMouse()
        shape.setFill(rgb)

    inst = Point(win_width / 2, win_height - 300)
    instructions = Text(inst, "Click again to close")
    instructions.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    text = input("enter a string: ")
    first_chr = text[0]
    last_chr = text[-1]
    cat = text[0:4] * 10
    length = len(text)
    print(first_chr)
    print(last_chr)
    print(text[2:6])
    print(first_chr + last_chr)
    print(cat)
    for char in text:
        print(char)
    print(length)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    pass


def target():
    win_width = 400
    win_height = 400
    win = GraphWin("Target", win_width, win_height)

    middle = Point(200, 200)

    center_circle = Circle(middle, 200)
    center_circle.setFill("white")
    center_circle.draw(win)

    target_circle = Circle(middle, 100)
    target_circle.setFill("red")
    target_circle.draw(win)

    inst = Point(win_width / 2, win_height - 200)
    instructions = Text(inst, "Click again to close")
    instructions.draw(win)

    win.getMouse()
    win.close()