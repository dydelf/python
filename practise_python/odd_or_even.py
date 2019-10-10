number = int(input("Please provide a number: "))

if number%2 == 0:
    print("This is an even number!")
    if number%4 == 0:
        print("It is also divisible by 4!")
else:
    print("It is an odd number :/")