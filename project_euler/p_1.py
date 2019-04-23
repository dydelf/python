#setting a range for example list
list_0 = range(1,500)
#multiplying every element from previous list by 3 and 5
list_1 = [3*x for x in list_0]
list_2 = [5*x for x in list_0]
#summing and sorting lists
list_3 = list_1 + list_2
list_3.sort()
#filtering a list to take out double numbers
list_4 = []
for i in list_3:
    if i not in list_4:
        list_4.append(i)
#taking out numbers in set range from a previous list
list_5 = []
for i in list_4:
    if i > 1000:
        break
    if i < 1000:
        list_5.append(i)
#summing numbers in a list
sum = sum(list_5)

print(sum)

#solution from archives

multiple_sum = 0

for i in range(1, 1000):
    if i % 3 == 0:
        multiple_sum += i
    elif i % 5 == 0:
        multiple_sum += i

print(multiple_sum)