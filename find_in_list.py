import timing

lst = list(range(99999999, 0, -1))

def find(x):
    checklist = []
    for i in lst:
        if i >= x:
            checklist.append(i)
    print(len(checklist))

#find(99999999)

def quick_find(x):
    checklist = []
    for i in lst and i >= x:
        checklist.append(i)
    print(len(checklist))

#quick_find(1)

#find(1)
print(lst.index(99999999) + 1)