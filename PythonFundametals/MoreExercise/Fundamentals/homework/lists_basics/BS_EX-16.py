capacity = 255
num = int(input())
full = 0
for x in range (num):
    leters = int(input())
    if (full + leters) > capacity:
        print ('Insufficient capacity!')
    else:
        full += leters
print (full)