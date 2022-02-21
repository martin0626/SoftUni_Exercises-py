mylist= [1,2,2,2,3,4,5,6,]

dup_items = set ()
uniq_items = []
for x in mylist:
    if x not in dup_items:
        uniq_items.append (x)
        dup_items.add(x)

print (dup_items)