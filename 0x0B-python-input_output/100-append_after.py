#!/usr/bin/python3
""" define a function that append text after a specific text """


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line containing a specific string
    """
    text = ""
    with open(filename) as fr:
        for line in fr:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as fw:
        fw.write(text)
