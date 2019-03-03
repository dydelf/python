#printing numbers and adding them until set amount
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#printing only numbers which are odd due to a continue function
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

