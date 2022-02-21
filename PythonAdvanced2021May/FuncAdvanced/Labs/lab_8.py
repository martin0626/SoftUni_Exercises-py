def expressions(nums, result=0, current_expression=''):
    if not nums:
        print(current_expression, result, sep='=')
        return
    expressions(nums[1:], result + nums[0], current_expression + f'+{nums[0]}')
    expressions(nums[1:], result - nums[0], current_expression + f'-{nums[0]}')


nums = [int(n) for n in input().split(', ')]
expressions(nums)
