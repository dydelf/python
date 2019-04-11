#modifying program to enter a flag

message = "Enter your message "
message += "\nwrite quit to exit"
message += "\nYour message - "
message_2 = ""

active = True
while active:
    message_2 = input(message)

    if message_2 == "quit":
        active = False
    else:
        print(message_2)




