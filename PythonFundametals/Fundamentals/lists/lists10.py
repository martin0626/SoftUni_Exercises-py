list1 = [1,2,3,4,5,6,7]
list2 = ['a','b','c','d']
boole = True
for x in list1:
    for y in list2:
        if x == y:
            print ('One item match!!')
            boole = False
            break
if boole:
    print ('No items match!!!')
        