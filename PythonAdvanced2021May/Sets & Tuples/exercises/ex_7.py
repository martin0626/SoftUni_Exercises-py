n = int(input())

even_nums = set()
odd_nums = set()

for row in range(1, n + 1):
    name = input()
    number = 0
    for char in name:
        number += ord(char)

    number = number // row

    if number % 2 == 0:
        even_nums.add(number)
    else:
        odd_nums.add(number)

if sum(even_nums) == sum(odd_nums):
    union = even_nums.union(odd_nums)
    print(", ".join([str(e) for e in union]))

elif sum(even_nums) < sum(odd_nums):
    different_nums = odd_nums.difference(even_nums)
    print(", ".join([str(e) for e in different_nums]))

else:
    symmetric_nums = even_nums.symmetric_difference(odd_nums)
    print(", ".join([str(e) for e in symmetric_nums]))
