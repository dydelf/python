from random import randint
#program generating a random number and you have to guess it

active = True
while active:
    try:
        print("Can you guess what number I generated in range 1-20? ")
        x = randint(1,20)
        answer = int(input())
        if answer < x:
            print("your answer is smaller than it should be!")
        elif answer > x:
            print("your answer is bigger than it should be!")
        else:
            print("You guessed correctly, the number is " + str(x))
            again = input("Would you like to play again? yes/no ")
            if again == 'no':
                active = False
            elif again == 'yes':
                print("Lets play again!")
                #trying to replay the loop but not from a beggining here
            else:
                break
    except ValueError:
        print("You have restarted program, please enter only numbers!")
        continue
