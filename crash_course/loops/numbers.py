for value in range(1,9):
	print(value)
	
numbers=list(range(1,10))
print(numbers)

numbers=list(range(2,20,3))
print(numbers)

squares=[]
for value in range(1,20):
	squares.append(value**2)
	
print(squares)

squares=[value**3 for value in range(1,10)]
print(squares)

numbers=list(range(1,9999))
print(numbers)
print(sum(numbers))
max(numbers)
sum(numbers)

