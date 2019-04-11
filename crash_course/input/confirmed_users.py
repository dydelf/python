#start with users that need to be verified
#and an empty list to add them
unconfirmed_users = ['Brian', 'Daniel', 'Nick']
confirmed_users = []

#verify each user
#move each verified user to new list
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

#Display all confirmed users
print("Following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
