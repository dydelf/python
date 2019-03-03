age = 3
if age <5:
    price = 0
elif age <18:
    price = 5
elif age <60:
    price = 10
elif age >=60:
    price = 5

print("Your price is: " + str(price) + " USD.")

if price >=5:
    print("Pay NOW!!!")
else:
    print("Have a nice trip :)")

