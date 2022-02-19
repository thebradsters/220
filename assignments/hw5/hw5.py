"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def name_reverse():
    myString = input("enter a name (first last): ")
    firstStr, lastStr = myString.split()
    comma = ","
    print(lastStr + str(comma), firstStr)


def company_name():
    domain = input("enter a domain: ")
    www, website, com = domain.split(".")
    print(website)


def initials():
    students = eval(input("how many students are in the class? "))
    for i in range(students):
        name = input(("what is the name of student? ", i + 1))
        firstStr, lastStr = name.split()
        print(firstStr[0] + str(lastStr[0]))


def names():
    names = input("enter a list of names: ")
    list = names.split()
    for initial in list:
        initial = initial[0]
        print(initial, end="")


def thirds():
    num_sentence = eval(input("enter the number of sentences: "))
    frag = ""
    for i in range(1, num_sentence + 1):
        sentences = input("enter sentence " + str(i) + ": ")
        length = len(sentences)
        frag = frag + sentences[0:length:3] + "\n"
    print(frag)


def word_average():
    sentence = input("enter a sentence: ")
    list = sentence.split()
    length = len(list)
    letters = "".join(list)
    word_length = len(letters)
    average = word_length / length
    print(average)


def pig_latin():
    sentence_input = input("enter a sentence to convert to pig latin: ")
    word = sentence_input.split()
    pig = "ay"
    for words in word:
        latin = words[1:] + words[0]
        p_l = latin + pig
        pig_latin = p_l.lower()
        final = pig_latin.rstrip()
        print(final, end=" ")


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
