"""
Write multiple lines to the file.
"""

file = open("multiple_lines.txt", "w")
list = [1, 2, 3, 4, 5]

for i in list:
    file.write(str(i) + "\n")
file.close()
