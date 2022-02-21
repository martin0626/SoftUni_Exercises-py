a = input()
b = input()
list_a = list(a)
list_b = list(b)
ind = 0
for index, item in enumerate(list_b):
    if item != list_a[ind]:
        list_a[ind] = list_b[index]
        for x in list_a:
            print (x, end = '')
        print()
    ind += 1
    

