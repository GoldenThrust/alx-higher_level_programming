#!/usr/bin/python3
""" text indentation """


def text_indentation(text):
    """ prints a text with 2 new lines after each 
    of these characters: ., ? and : """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chx = 0
    for txt in text:
        if chx == 0:
            if txt == " ":
                continue
            else:
                chx = 1
        if chx == 1:
            if txt in ".?:":
                print(txt)
                print()
                chx = 0
            else:
                print(txt, end="")
