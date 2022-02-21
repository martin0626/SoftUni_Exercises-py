numbers = input().split(', ')
numbers = list(map(int, numbers))
factor = 10
while not len(numbers) == 0:
    list_of_each = []
    
    
    for x in numbers:

        if int(x) <= factor:
            list_of_each.append(x)
    for y in list_of_each:
        numbers.remove(y)
    print (f"Group of {factor}'s: {list_of_each}")
    factor += 10
    list_of_each.clear()