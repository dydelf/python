my_foods=['chicken', 'salad', 'fruit']
friends_foods=my_foods[:]

print(my_foods)
print(friends_foods)

my_foods.append('curry')
friends_foods.append('soup')

print(my_foods)
print(friends_foods)

print("\nMy absolute best are: " + str(my_foods[1:3]))
print("His best foods are: " + str(friends_foods[2]))

print("\nMy favourite foods are:")
for my_food in my_foods:
    print(my_food)
print("\nHis foods are:")
for friend_food in friends_foods:
	print(friend_food)
	


	
    
