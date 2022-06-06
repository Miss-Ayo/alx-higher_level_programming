#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    character = sentence[0]
    if lenght < 0:
        return None
    else:
        return (lenght, character)
