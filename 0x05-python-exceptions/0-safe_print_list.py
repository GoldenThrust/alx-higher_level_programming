#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    for j in range(x):
        try:
            print(my_list[m], end="")
            i++
        except IndexError:
            break
    print()
    return i
