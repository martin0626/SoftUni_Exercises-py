people = int(input())
capacity = int(input())
if people <= capacity:
    print ('1')

else:
    if people % capacity == 0:
        print (people // capacity)
    else:
        print (people // capacity + 1)