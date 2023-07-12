#!/usr/bin/python3
""" define function that read file """


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout: """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
