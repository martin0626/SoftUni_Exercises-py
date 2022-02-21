type_int = input()
nums = [int(e) for e in input().split()]

if type_int == 'Odd':
    odd_nums = list(filter(lambda x: x % 2 != 0, nums))
    print(sum(odd_nums) * len(nums))

else:
    even_nums = list(filter(lambda x: x % 2 == 0, nums))
    print(sum(even_nums) * len(nums))
