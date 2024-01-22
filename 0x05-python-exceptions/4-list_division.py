#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []

    for x in range(list_length):
        index = 0
        try:
            index = my_list_1[x] / my_list_2[x]
        except IndexError:
            print("out of range")
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            new.append(index)
    return new
