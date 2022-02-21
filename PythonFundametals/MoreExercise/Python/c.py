n = input()
s = 0
c = 0
while n != 'stop':
    
    n = float(n)
    s += n
    c += 1
    n = input()
end_sum = s / c
print (f'{end_sum:.2f}')


