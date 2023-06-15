#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list and len(my_list):
        nums, dems = 0
        for i, j in my_list:
            nums += i * j
            dems += j
        return (nums / dems)
    return 0
