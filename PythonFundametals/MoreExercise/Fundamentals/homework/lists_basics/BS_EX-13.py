n = int(input())
sum_total = 0
for x in range (n):
    letter = input()
    sum_total += ord(letter)

print (f'The sum equals: {sum_total}')
