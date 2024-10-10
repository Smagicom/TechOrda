#!/usr/bin/env python3

def pallindrom(w):
    reversed_word = w[::-1]
    if not w:  # Check for empty string
        raise ValueError("Input cannot be empty!")
    if w == reversed_word:
        print("This word is pallindrom!")
    else:
        print("This word is not pallindrom!") 

w = input("Please enter a word: ")
pallindrom(w)
