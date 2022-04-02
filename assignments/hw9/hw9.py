from random import randint


def get_words(file_name):
    in_file = open(file_name, "r")
    read_file = in_file.readlines()
    return read_file


def get_random_word(words):
    random_word = randint(0, len(words) - 1)
    secret_word = words[random_word]
    return secret_word.rstrip()


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    return False


def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    return False


def make_hidden_secret(secret_word, guesses):
    word = ""
    for i in range(len(secret_word)):
        for j in range(len(guesses)):
            if guesses[j] == secret_word[i]:
                word = word + guesses[j]
        if not len(word) == i + 1:
            word = word + "_"
    space = ""
    for i in range(len(word)):
        space = space + " " + word[i]
    return space.lstrip()


def won(guessed):
    if '_' in guessed:
        return False
    return True


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    pass


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
