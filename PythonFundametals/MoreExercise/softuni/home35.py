n = int(input())

for x in range (1, 10):
    
    for y in range (1, 10):
       
        for z in range (1, 10):
            
            for j in range (1, 10):
                if n % j == 0 and n % z == 0 and n % y == 0 and n % x == 0: 
                    print (f'{x}{y}{z}{j}', end = ' ')
