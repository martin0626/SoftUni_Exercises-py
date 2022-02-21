d = int(input())
m = int(input())
d_in_m = 31

if m == 2:
    d_in_m = 28

if m == 4 or m == 6 or m == 9 or m == 11:
    d_in_m = 30

d += 5

if d_in_m < d:
    d -= d_in_m
    m += 1
    if m > 12:
        m = 1
print ('%d.%02d' % (d, m))
