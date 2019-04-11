#creating a poll which mountain who would like to climb

responses = {}
active = True

while active:
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb? ")

    #storing answer in a dictionary
    responses[name] = response

    repeat = input("Anyone else would like to answer? yes/no ")
    if repeat == "no":
        active = False

#polling complete
print(responses)
print("\n")
for name, response in responses.items():
    print(name + " would like to climb: " + response)
    