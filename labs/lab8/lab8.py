from random import randint
from graphics import *
import math
import time


def bumper():
    width_px = 700
    height_px = 700
    win = GraphWin("Joyride Testing App", width_px, height_px)
    win.setBackground("white")

    point_one = Point(300, 500)
    circle_ball = Circle(point_one, 30)
    circle_ball.setFill("#{}".format(get_random_color()))
    circle_ball.draw(win)

    point_two = Point(500, 500)
    circle_ball2 = Circle(point_two, 30)
    circle_ball2.setFill("#{}".format(get_random_color()))
    circle_ball2.draw(win)

    x1_vel = get_random(8)
    x2_vel = get_random(8)
    y1_vel = get_random(8)
    y2_vel = get_random(8)

    while True:
        circle_ball.move(x1_vel, y1_vel)
        circle_ball2.move(x2_vel, y2_vel)
        if did_collide(circle_ball, circle_ball2):
            x1_vel = x1_vel * -1
            x2_vel = x2_vel * -1
            y1_vel = y1_vel * -1
            y2_vel = y2_vel * -1
        if hit_vertical(circle_ball, 700):
            x1_vel = x1_vel * -1
        if hit_vertical(circle_ball2, 700):
            x2_vel = x2_vel * -1
        if hit_horizontal(circle_ball, 700):
            y1_vel = y1_vel * -1
        if hit_horizontal(circle_ball2, 700):
            y2_vel = y2_vel * -1
        time.sleep(.02)


def get_random(move_amount):
    random_num = randint(-move_amount, move_amount)
    return random_num


def did_collide(circle_ball, circle_ball2):
    center_x = (circle_ball2.getCenter().getX() - circle_ball.getCenter().getX()) ** 2
    center_y = (circle_ball2.getCenter().getY() - circle_ball.getCenter().getY()) ** 2
    distance = math.sqrt(center_x + center_y)
    radius_1 = circle_ball.getRadius()
    radius_2 = circle_ball2.getRadius()
    radius_sum = radius_2 + radius_1
    if distance <= radius_sum:
        return True
    return False


def hit_vertical(circle_ball, win):
    if circle_ball.getCenter().getX() + circle_ball.getRadius() >= win:
        return True
    if circle_ball.getCenter().getX() - circle_ball.getRadius() <= 0:
        return True
    return False


def hit_horizontal(circle_ball, win):
    if circle_ball.getCenter().getY() + circle_ball.getRadius() >= win:
        return True
    if circle_ball.getCenter().getY() - circle_ball.getRadius() <= 0:
        return True
    return False


def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return ('{:02X}' * 3).format(r, g, b)


if __name__ == '__main__':
    bumper()
