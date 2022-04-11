from lab10.button import Button
from lab10.door import Door
from graphics import *
from random import randint


def main():
    win_length = 800
    win_height = 800
    win = GraphWin("Three Door Game", win_length, win_height)
    win.setBackground("light blue")

    exit_p1 = Point(640, 30)
    exit_p2 = Point(760, 100)
    exit_button = Button(Rectangle(exit_p1, exit_p2), "Quit")
    exit_button.draw(win)

    door1_p1 = Point(50, 250)
    door1_p2 = Point(250, 700)
    door_1 = Door(Rectangle(door1_p1, door1_p2), "Door 1")
    door_1.draw(win)
    door_1.color_door("saddle brown")

    door2_p1 = Point(300, 250)
    door2_p2 = Point(500, 700)
    door_2 = Door(Rectangle(door2_p1, door2_p2), "Door 2")
    door_2.draw(win)
    door_2.color_door("saddle brown")

    door3_p1 = Point(550, 250)
    door3_p2 = Point(750, 700)
    door_3 = Door(Rectangle(door3_p1, door3_p2), "Door 3")
    door_3.draw(win)
    door_3.color_door("saddle brown")

    wins_p1 = Point(40, 30)
    wins_p2 = Point(120, 100)
    wins_button = Rectangle(wins_p1, wins_p2)
    wins_center = wins_button.getCenter()
    win_text = Text(wins_center, "0")
    wins_button.draw(win)
    win_text.draw(win)

    losses_p1 = Point(120, 30)
    losses_p2 = Point(200, 100)
    losses_button = Rectangle(losses_p1, losses_p2)
    losses_center = losses_button.getCenter()
    loss_text = Text(losses_center, "0")
    loss_text.draw(win)
    losses_button.draw(win)

    wins_msg = "Wins"
    wins_text = Text(Point(80, 20), wins_msg)
    wins_text.draw(win)

    losses_msg = "Losses"
    losses_text = Text(Point(160, 20), losses_msg)
    losses_text.draw(win)

    inst_1 = "I have a secret door"
    inst_txt = Text(Point(400, 750), inst_1)
    inst_txt.draw(win)

    inst_2 = "Click to guess which is the secret door!"
    inst_2_txt = Text(Point(400, 200), inst_2)
    inst_2_txt.draw(win)

    doors = [door_1, door_2, door_3]

    winner = 0
    loser = 0
    mouse = win.getMouse()
    while not exit_button.is_clicked(mouse):
        secret = randint(0, 2)
        doors[secret].set_secret(True)
        for door in doors:
            if door.is_clicked(mouse):
                if door.is_secret():
                    door.color_door("Green")
                    winner += 1
                    win_text.setText(str(winner))
                else:
                    door.color_door("Red")
                    loser += 1
                    loss_text.setText(str(loser))
            elif door.is_secret():
                door.color_door("Green")
        inst_txt.setText("Click anywhere to play again")
        mouse = win.getMouse()
        if exit_button.is_clicked(mouse):
            break
        doors[secret].set_secret(False)
        for door in doors:
            door.color_door("Saddle brown")
        inst_txt.setText("I have a secret door")
        mouse = win.getMouse()

    win.close()


if __name__ == "__main__":
    main()