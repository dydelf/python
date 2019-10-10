name = input("What is your name?: ")
age = input("What is your age?: ")

prediction = (100 - int(age)) + 2019

print("Hello " + name + "!")
var = "You will turn 100 years old in " + str(prediction) + " year!"
print(var)

number = int(input("Please provide a number: "))

for i in range(number):
    print(var)
