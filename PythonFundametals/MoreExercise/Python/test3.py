n = int(input())
current_long = 0
count_longest = 0
prev_num = 0




for x in range (n):
    num = int(input())
    if num > prev_num:
        bigger_num = num
        current_long += 1

    else:
        current_long = 1

    if current_long > count_longest:
        count_longest = current_long

    prev_num = num

print (count_longest)