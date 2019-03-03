existing_usernames = ['paul', 'dorothy', 'michael', 'sylvia', 'nick']
new_usernames = ['dorothy', 'arthur', 'paul', 'justin', 'maverick']
current_users = ['admin', 'arthur', 'paul', 'michael']



if current_users:
    for current_user in current_users:
        if current_user == 'admin':
            print('Welcome master!\n') 
        else:
            if current_user in existing_usernames:
                print("Welcome old user - " + current_user.title())
            else:
                if current_user in new_usernames:
                    print("Hello new user - " + current_user.title())
                if current_user in existing_usernames:
                    print("This username is already used, please change it!\n")
else:
    print("Where are the users?!")

print('Test EOFError')