#!/usr/bin/python3
for i in range(9):
    for j in range(9):
        if j >= i:
            print("{}{}".format(i, j), end=", ")
print('99', end="\n")
