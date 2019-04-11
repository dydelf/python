"""
simple exception handling
"""

filename = 'alice.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, couldn't find the file"
    print(msg)
else:
    #count words in a file text
    words = contents.split()
    num_words = len(words)
    print("The file has approximately " + str(num_words) + " words")
