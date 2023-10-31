#!/usr/bin/python3

current = 0
ascii_num = 122

for i in range(26):
    if ascii_num == 122 and current == 0:
        ascii_num = 122
        current = 1
    elif current == 1:
        ascii_num -= 33
        current = 0
    elif current == 0:
        ascii_num += 31
        current = 1
    print("{}".format(chr(ascii_num)), end="")
