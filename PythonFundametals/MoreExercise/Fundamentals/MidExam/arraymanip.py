nums = [int(x) for x in input().split()]


command = input()

while command != 'end':
    command = command.split()
    if command[0] == 'swap':
        nums[int(command[1])], nums[int(command[2])] = nums[int(command[2])], nums[int(command[1])]

    elif command[0] == 'multiply':
        nums[int(command[1])] = nums[int(command[1])] * nums[int(command[2])]
    
    else:
        nums = [x-1 for x in nums]
    command = input()
nums = list(map(str, nums))
print (', '.join(nums))