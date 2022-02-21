import re
mylist = []
counter = 0


while True:
    a = input()
    
    if a == 'correct':
        counter += 1
        for n in range (counter):
            mylist.append(n + 1)
        
    if counter >= 5:
        break
    
    
    
for x in mylist:
    print (x)