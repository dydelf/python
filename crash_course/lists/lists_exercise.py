#lists of invitation
guests = ['natalia', 'konrad', 'karol', 'mateusz']
print("Zaproszenie dla: " + guests[0])
print("Zaproszenie dla: " + guests[1])
print("Zaproszenie dla: " + guests[2])
print("Zaproszenie dla: " + guests[3])

print("\nO nie karol nie moze przyjsc!")
guests.remove('karol')
print(guests)

print("\nDamian przyjdzie na jego miejsce")
guests.insert(2, "damian")
print(guests)

print("\nZaproszenie dla: " + guests[0])
print("Zaproszenie dla: " + guests[1])
print("Zaproszenie dla: " + guests[2])
print("Zaproszenie dla: " + guests[3])

#dodawanie wiecej gosci

guests.append('karolina')
guests.append('patryk')
guests.append('kinga')
guests.append('sylwia')

print("\n")
print(guests)

print("\nZaproszenie dla: " + guests[0])
print("Zaproszenie dla: " + guests[1])
print("Zaproszenie dla: " + guests[2])
print("Zaproszenie dla: " + guests[3])
print("Zaproszenie dla: " + guests[4])
print("Zaproszenie dla: " + guests[5])
print("Zaproszenie dla: " + guests[6])
