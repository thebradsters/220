def encode(message, key):
    length = len(message)
    my_string = ""
    for i in range(length):
        letter = message[i]
        encoded = ord(letter) + key
        decoded = chr(encoded)
        my_string = my_string + decoded
    return my_string

def encode_better():
    message = input("enter a message: ")
    key = input("enter a key: ")
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
        encode_mod = (both_encoded % 58) + 65
        decoded = chr(encode_mod)
        my_string = my_string + decoded
    print(my_string)