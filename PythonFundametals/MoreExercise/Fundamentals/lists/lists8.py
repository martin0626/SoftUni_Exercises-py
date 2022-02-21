mylist = [1,2,3,4,5,6,78,8]
newlist = []

num = None
while num != 'Stop':
    num = input()
    newlist.append(num)
    if num == 'Stop':
        newlist.pop()

if len(mylist) > len(newlist):
    print (mylist)
else: 
    print (newlist)
