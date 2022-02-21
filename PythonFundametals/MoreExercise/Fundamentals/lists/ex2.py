mylist = []
factor = int(input())
count = int(input())
counter = 0 
for x in range (1, 100000):
    if counter == count:
        break
    
    if x % factor == 0:
        mylist.append(x)
        counter += 1

print (mylist)
    