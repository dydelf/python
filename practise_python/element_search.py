import timing

ordered_list = list(range(1, 100000))
x = 9999
#x = int(input("Type an integer to check if it's in a list: "))

def find_number_binary(ordered_list, x):
    """Find number in an ordered list. """
    flag = True
    while flag:
        half = len(ordered_list)//2
        if ordered_list[half] >= x:
            ordered_list = ordered_list[:(half+1)]
        else:
            ordered_list = ordered_list[half:]
        
        if len(ordered_list) < 5:
            for i in ordered_list:
                if i == x:
                    return print(True)
            else:
                return print(False)


def find_number(ordered_list, x):
    """Find number in an ordered list. """
    for i in ordered_list:
        if i == x:
            return print(True)
    return print(False)


# Python Program for recursive binary search.

# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):

    # Check base case
    if r >= l:

        mid = int(l + (r - l)/2)

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


# Function call
result = binarySearch(ordered_list, 0, len(ordered_list)-1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")

#find_number(ordered_list, x)
#find_number_binary(ordered_list, x)
