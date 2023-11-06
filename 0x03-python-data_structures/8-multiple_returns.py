#!/usr/bin/python3

def multiple_returns(sentence):
    strlen = len(sentence)

    if strlen == 0:
        return strlen, None

    return strlen, sentence[0]
