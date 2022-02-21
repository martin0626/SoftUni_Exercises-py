text = input().split('|')
result = [[int(n) for n in nums.split()] for nums in reversed(text)]
print(*[n for l in result for n in l])
