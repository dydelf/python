#simple exercise of printing and adding elements of the list
motorcycles = ['ducati', 'honda', 'yamaha']
print(motorcycles)

motorcycles[0] = 'bmw'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'kawasaki')
print(motorcycles)

del motorcycles[4]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(motorcycles[0])

#removing an item from the list if you know the name and not the location

motorcycles.remove('honda')
print(motorcycles)

