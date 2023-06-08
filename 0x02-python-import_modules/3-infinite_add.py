#!/usr/bin/python3

if __name__ = "__main__":
    import sys as s

    t = 0
    for i in range(len(s.argv) - 1):
        t += int(s.argv[i + 1])
    print("{}".format(t))
