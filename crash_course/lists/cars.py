cars = ['toyota', 'bmw', 'subaru', 'skoda']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
x = 10
print(x)
print(12)

#sorting the list temporarily
print("this is the original list:\n")
cars.sort(reverse=True)
print(cars)

print("this is sorted list:")
print(sorted(cars))

print("and original again")
print(cars)

print(cars[0].title())

length = len(cars)
print(length)

numbers = [8,6,3,65,113,456]
print(numbers)
print(sorted(numbers))
numbers.sort()
print(numbers)



