n = int(input())
l = int(input())

for x in range (1, n + 1):
    for y in range (1, n + 1):
        for z in range (61, 61 + l):
            z = chr(z)
            for u in range (61, 61 + l):
                u = chr(u)
                print (x,y,end = '') 