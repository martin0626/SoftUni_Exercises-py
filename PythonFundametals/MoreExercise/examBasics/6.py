
first = int(input())
last = int(input())
first = str(first)
last = str(last)

for x in range (int(first[0]), int(last[0]) + 1):
    for y in range (int(first[1]), int(last[1]) + 1):
        for z in range (int(first[2]), int(last[2]) + 1):
            for n in range (int(first[3]), int(last[3]) + 1):
                if x % 2 != 0 and y % 2 != 0 and z % 2 != 0 and n % 2 != 0:
                    print (f'{x}{y}{z}{n}', end = ' ')

    
