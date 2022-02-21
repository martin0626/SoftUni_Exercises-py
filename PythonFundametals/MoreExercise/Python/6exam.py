mark_num = int(input())
fin_mark_end = 0
mark_count = 0
end = 0
while True:
    
    lec = input()
    if lec == 'Finish':
        print (f'End mark is {end / 2mark_count :.2f}')
        break
    mark_sum = 0

    for x in range (mark_num):
        mark = float(input())
        mark_sum += mark
        fin_mark = mark_sum / mark_num
    mark_count += 1
    end += fin_mark

    print (f'{lec} - {fin_mark}')

        
