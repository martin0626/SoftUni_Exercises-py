numbers = input().split()
to_remove = int(input())
new_list = []

for y in numbers:
     y = int(y)
     new_list.append(y)
for x in range (to_remove):    
    #new_list.sort()
    #new_list.pop(0)
    new_list.remove(min(new_list))
    
print (new_list)

