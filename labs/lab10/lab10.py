from graphics import *
from button import Button
from door import Door


def three_door_game():
    win_length = 400
    win_height = 400
    win = GraphWin("Test", win_length, win_height)
    win.setBackground("gray")

    p1 = Point(100, 25)
    p2 = Point(300, 100)
    butt = Button(Rectangle(p1, p2), "Exit")
    butt.draw(win)

    door_p1 = Point(100, 125)
    door_p2 = Point(300, 400)
    door = Door(Rectangle(door_p1, door_p2), "Closed")
    door.draw(win)
    door.color_door("red")

    mouse = win.getMouse()
    while not butt.is_clicked(mouse):
        if door.is_clicked(mouse):
            label = door.get_label()
            if label == "Open":
                door.close("red", "Closed")
            else:
                door.open("white", "Open")
        mouse = win.getMouse()

    win.close()


if __name__ == "__main__":
    three_door_game()
