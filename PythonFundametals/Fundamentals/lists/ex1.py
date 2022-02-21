mylist = []
nums = input()
spl = nums.split()
#mylist.append(spl[0])

for x in spl:
    x = int(x) * -1
    mylist.append(x)

print (mylist)

