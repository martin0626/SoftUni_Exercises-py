nums = [int(n) for n in input().split(', ')]
print('Positive:', ', '.join([str(n) for n in nums if n >= 0]))
print('Negative:', ', '.join([str(n) for n in nums if n < 0]))
print('Even:', ', '.join([str(n) for n in nums if n % 2 == 0]))
print('Odd:', ', '.join([str(n) for n in nums if n % 2 != 0]))
