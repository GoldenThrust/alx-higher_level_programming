#!/usr/bin/python3

if __name__ == "__main__":
    import sys as s

    c_num = len(s.argv) - 1
    if c_num == 0:
        print("0 argument.")
    elif c_num == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(c_num))
    for i in range(c_num):
        print("{}: {}".format(i + 1, s.argv[i + 1]))
