"""
Get the definition of typed in word.
"""

import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        print("\nDid you mean %s instead?" % get_close_matches(word,
            data.keys(), cutoff=0.8)[0])
        word = get_close_matches(word, data.keys(), cutoff=0.8)[0]
        return data[word]
    else:
        return "The word doesn't exist. Please double check it."

active = True
while active:
    print("Get the definition of the word.")
    word = input("Enter word: ")
    output = translate(word)
    print("\n")
    if type(output) == str:
        print(output)
    else:
        for i in output:
            print(i)
    flag = input("\nWould you like another word? | y/n | ")
    if flag == "n":
        active = False
    else:
        active = True
