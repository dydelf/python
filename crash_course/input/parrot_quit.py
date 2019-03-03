message = "Enter your message "
message += "\nwrite quit to exit"
message += "\nYour message - "

message_2 = ""
while message_2 != "quit":
    message_2 = input(message)

    if message_2 != "quit":
        print(message_2)


