#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds all the even numbers in a list
    """
    if my_list:
        list_length = len(my_list)
        new_list = []
        for number in range(list_length):
            if my_list[number] % 2 == 0:
                new_list.insert(number, True)
            else:
                new_list.insert(number, False)
        return new_list
