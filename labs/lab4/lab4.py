from graphics import *
import time

def greeting_card():
    width = 1000
    height = 1000
    win = GraphWin("Greeting Card", width, height)
    p_1 = Point(550, 800)
    p_2 = Point(800, 450)
    p_3 = Point(650, 250)
    p_4 = Point(550, 375)
    p_5 = Point(450, 250)
    p_6 = Point(300, 450)

    arrow = Line(Point(700, 700), Point(500, 500))
    arrow.setOutline("black")
    arrow.setFill("black")
    arrow = arrow.clone()
    arrow.draw(win)

    tip = Polygon(Point(500, 500), Point(490, 510), Point(510, 490), Point(480, 480), Point(490, 510))
    tip.setOutline("black")
    tip.setFill("black")
    tip = tip.clone()
    tip.draw(win)

    heart = Polygon(p_1, p_2, p_3, p_4, p_5, p_6)
    heart.setOutline("red")
    heart.setFill("red")
    heart = heart.clone()
    heart.draw(win)

    text = Point(550, 475)
    msg = Text(text, "Happy Valentine's Day!")
    msg.draw(win)

    for i in range(35):
        arrow.move(-10, -10)
        tip.move(-10, -10)
        time.sleep(0.1)

    end = Point(550, 500)
    end_msg = Text(end, "Click to close")
    end_msg.draw(win)

    win.getMouse()
    win.close()



greeting_card()