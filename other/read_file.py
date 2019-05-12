"""
Reading contents of the file.
"""

fruits = open("fruits.txt", "r")
content = fruits.readlines()
content = [i.rstrip("\n") for i in content]
print(content)

for i in content:
    print(len(i.strip()))

fruits.close()
