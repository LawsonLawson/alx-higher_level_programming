#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    current_index = 0
    for char in str:
        if current_index != n:
            new_str += char
        current_index += 1
    return new_str
