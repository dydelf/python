#creating a list using list comprehension and mathematical formula for
#golden ratio to fibbonacci sequence
fib = [int((((1 + 5**0.5) / 2)**n - 
    ((1 - 5**0.5) / 2)**n) / 5**0.5) for n in range(1, 999)]

#selecting only even values lesser than 4 milion
fib_2 = [i for i in fib if i < 4000000 and i % 2 ==0]
print(fib_2)

#summing up all the values
print(sum(fib_2))
