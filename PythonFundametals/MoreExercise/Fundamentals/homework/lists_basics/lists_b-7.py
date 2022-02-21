numbers = input().split(', ')
beggars = int(input())
list_beggars = []
for beggar in range (0, beggars):
    sum_beggar = 0
    for num in range (beggar, len(numbers), +beggars):
        sum_beggar += int(numbers[num])
    list_beggars.append(sum_beggar)
    
print (list_beggars)

