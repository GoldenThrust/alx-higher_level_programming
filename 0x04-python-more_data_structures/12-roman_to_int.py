#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 100
            }
    dec_list = [roman_dict[i] for i in roman_string]
    val = 0
    for i in range(len(dec_list)):
        val += dec_list[i]
        if i != 0 and dec_list[i - 1] < dec_list[i]:
            val -= (dec_list[i - 1] * 2)
    return val
