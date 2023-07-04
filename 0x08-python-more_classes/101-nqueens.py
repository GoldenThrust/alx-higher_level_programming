#!/usr/bin/python3

"""
nqueen backtracing
"""

from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueen N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    if int(argv[1]) < 4:
        print("N must be at least 4")
        exit(1)
    board = []
    [board.append([]) for i in range(int(argv[1]))]
    [row.append(None) for i in range(int(argv[1])) for row in board]
