#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        return None
    else:
        lenght = len(sentence)
        character = sentence[0]
        return (lenght, character)
