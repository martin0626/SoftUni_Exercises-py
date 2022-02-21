n = int(input())
l = int(input())

for symbol_1 in range (1, n + 1):
    for symbol_2 in range (1, n + 1):
        for symbol_3 in range (97, 97 + l):
            symbol_3 = chr(symbol_3)
            for symbol_4 in range (97, 97 + l):
                symbol_4 = chr(symbol_4)
                for symbol_5 in range (symbol_1 + 1, n + 1):
                    if symbol_2 < symbol_5 and symbol_1 < symbol_5:
                        print (f'{symbol_1}{symbol_2}{symbol_3}{symbol_4}{symbol_5}', end = ' ')
                        

                    
