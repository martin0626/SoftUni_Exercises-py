a = input()
n = int(input())
b = a.split()
c = ''
for x in b:
    ste = len(x)
    if ste > n:
        c += x


print (c)