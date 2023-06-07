#!/usr/bin/python3

for i in range(8):
    for j in range(i + 1, 10):
        print(f"{i}{j}", end=", ")
print(f"{i+1}{j}")
