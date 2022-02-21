mylist = []
x = None

while x != 'End':
    x = input()
    mylist.append(x)
    if x == 'End':
        mylist.pop(-1)

print (mylist)