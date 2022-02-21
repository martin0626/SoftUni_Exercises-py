nums = [int(x) for x in input().split()]

average = sum(nums) / len(nums)

top_numbers = [num for num in nums if num > average]
top_numbers = sorted(top_numbers, reverse=True)
top_numbers = [str(x) for x in top_numbers]
if len(top_numbers) == 0:
    print ('No')
else:   
    if len(top_numbers) < 5:
        print (' '.join(top_numbers))
    else:
        top_numbers = top_numbers[0:5]
        print (' '.join(top_numbers))

