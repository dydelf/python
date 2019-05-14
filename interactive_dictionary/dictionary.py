"""
Get the definition of typed in word.
"""

import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def translate(word):
    word = word.lower()
    if word in data:
        for i in data[word]:
            print(i)
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        print("\nDid you mean %s instead?" % get_close_matches(word,
            data.keys(), cutoff=0.8)[0])
        word = get_close_matches(word, data.keys(), cutoff=0.8)[0]
        for i in data[word]:
            print(i)
    else:
        return "The word doesn't exist. Please double check it."

active = True
while active:
    word = input("Enter word: ")
    print("\n")
    print(translate(word))
    flag = input("\nWould you like another word? | y/n | ")
    if flag == "n":
        active = False
    else:
        active = True
