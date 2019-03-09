filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Type your birthdate in format ddmmyy: ")
if birthday in pi_string:
    print("your birthdate apear in the first milion digits of pi!")
else:
    print("I am sorry, you are unlucky")
