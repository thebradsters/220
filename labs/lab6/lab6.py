from graphics import *


def vigenere():
    win_width = 600
    win_height = 400
    win = GraphWin("Vigenere", win_width, win_height)
    win.setBackground("white")

    msg_code = "Message to code:"
    msg_code_inst = Text(Point(100, 70), msg_code)
    msg_entry = Entry(Point(250, 70), 20)
    msg_entry.draw(win)
    msg_code_inst.draw(win)

    key_msg = "Enter Keyword:"
    key_inst = Text(Point(100, 100), key_msg)
    key_entry = Entry(Point(250, 100), 20)
    key_entry.draw(win)
    key_inst.draw(win)

    shape = Rectangle(Point(200, 125), Point(275, 165))
    shape_msg = "Encode"
    shape_inst = Text(Point(235, 145), shape_msg)
    shape.draw(win)
    shape_inst.draw(win)

    win.getMouse()

    message = msg_entry.getText()
    message = message.upper().replace(" ", "")

    key = key_entry.getText()
    key = key.upper().replace(" ", "")

    length = len(message)
    key_length = len(key)
    my_string = ""
    for i in range(length):
        letter = message[i]
        number_key = i % key_length
        letter_key = key[number_key]
        encoded = ord(letter) - 65
        key_encoded = ord(letter_key) - 65
        both_encoded = encoded + key_encoded
        encode_mod = (both_encoded % 26) + 65
        decoded = chr(encode_mod)
        my_string = my_string + decoded

    shape.undraw()
    shape_inst.undraw()

    result_msg = "Resulting Message:\n"
    shape_inst.setText(result_msg + my_string)
    shape_inst.draw(win)

    close_msg = "Click Anywhere to Close Window"
    close_inst = Text(Point(win_width / 2, win_height - 40), close_msg)
    close_inst.draw(win)

    win.getMouse()
    win.close()

vigenere()
