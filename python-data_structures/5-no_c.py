#!/usr/bin/python3

def no_c(my_string):
    result = ''
    for letter in my_string:
        if letter == 'c' or letter == 'C':
            continue

        result = result + letter

    return result
