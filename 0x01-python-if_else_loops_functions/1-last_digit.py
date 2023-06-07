#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = (-(abs(number) % 10) if number < 0 else (abs(number) % 10))
if l == 0:
    print(f"Last digit of {number:d} is {l:d} and is 0")
elif l < 6:
    print(f"Last digit of {number:d} is {l:d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {l:d} and is greater than 5")
