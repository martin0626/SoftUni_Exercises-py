int_one = int(input())
int_two = int(input())
sum_one = 1
sum_two = 1
for x in range (1, int_one + 1):
    sum_one *= x
for y in range (1, int_two + 1):
    sum_two *= y

print (f'{(sum_one / sum_two):.2f}')
