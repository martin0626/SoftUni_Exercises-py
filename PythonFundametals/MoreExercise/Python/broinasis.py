x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

def triangel_h (y1, y2):
    h = abs (y1 - y2)
    return h

def triangel_a (x2, x3):
    a = abs (x2 - x3)
    return a

print (triangel_a(y1, y2) * triangel_h(x2, x3) / 2)


