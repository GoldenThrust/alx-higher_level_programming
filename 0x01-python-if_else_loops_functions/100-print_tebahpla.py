#!/usr/bin/python3

alt = 0
for i in range(ord("z"), ord("a") - 1, -1):
    print(f"{chr(i - alt)}", end="")
    alt = 32 if alt == 0 else 0
