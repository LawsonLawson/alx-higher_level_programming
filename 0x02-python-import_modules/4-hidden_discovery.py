#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    the_names = dir(hidden_4)
    for name in the_names:
        if name[0:2] != "__":
            print(name)
