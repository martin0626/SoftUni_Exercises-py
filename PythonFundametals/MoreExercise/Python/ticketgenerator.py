n = int(input())
ascii_sum = 0
counter = 0
   
    
for furst_buk in range (ord('B'), ord('L') + 1, +2):
    for second_buk in range (ord('f'), ord('a')-1, -1):
        for third_buk in range (ord('A'), ord('C') + 1):
            for furst_num in range (1, 11):
                for second_num in range (10, 0, -1):
                    ascii_sum = furst_buk + second_buk + third_buk + furst_num + second_num
                    counter += 1
                    if counter == n:
                        print (f'Ticket combination is {chr(furst_buk)}{chr(second_buk)}{chr(third_buk)}{furst_num}{second_num}')
                        print (ascii_sum)