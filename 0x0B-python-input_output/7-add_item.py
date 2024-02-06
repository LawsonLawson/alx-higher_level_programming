#!/usr/bin/python3
"""
Module: 7-add_item.py

Description: This module features a script that adds all arguments to
a python list, and then save them to a file.
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    file = 'add_item.json'
    try:
        obj = load_from_json_file(file)
    except Exception as i:
        obj = []
    save_to_json_file(obj + argv[1:], file)
