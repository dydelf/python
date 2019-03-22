"""
calculating a 30 day 1 cent coin multiplying
"""

def main():
    num_input = int(input('How many days do you have? '))
    # Accumulate the total
    total = 0.01
    for day_num in range(num_input):
        if day_num == 0:
            print("Day: ", day_num, end=' ')
            total = total
            print("the pennies today are:", total)
            day_num += day_num
        else:    
            print("Day: ", day_num + 1, end=' ')
            total += 2 * total
            print("the pennies today are:", total)         
main()

