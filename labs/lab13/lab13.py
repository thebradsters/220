from algorithms import *


def trade_alert(filename):
    in_file = open(filename, 'r')
    my_list = []
    line = in_file.read().split()

    for i in line:
        my_list.append(float(i))
    for i in range(len(my_list)):
        if my_list[i] > 830:
            print('warning exceeded 830 at', i + 1, 'seconds \n')
        elif my_list[i] == 500:
            print('alert equals 500 at', i + 1, 'seconds \n')
    in_file.close()


if __name__ == '__main__':
    binary_data = [-2, 10, 3, -9, 20, 19]
    binary = is_in_binary(20, binary_data)
    print(binary)

    rectangle_list = [Rectangle(Point(7, 8), Point(9, 10)), Rectangle(Point(1, 2), Point(3, 4))]
    rect_sort(rectangle_list)
    print(rectangle_list)

    trade_alert('trades.txt')

