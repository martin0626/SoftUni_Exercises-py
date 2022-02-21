numbers = input().split()

def manipulator (num):
    even_nums = []
    odd_nums = []
    
    
    for x in num:
        x = int(x)
        if x % 2 == 0:
            even_nums.append(x)
        else:
            odd_nums.append(x)
    
    if len(even_nums) > 0:
        max_even = max(even_nums)
        min_even = min(even_nums)
    if len(odd_nums) > 0:
        max_odd = max(odd_nums)
        min_odd = min(odd_nums)
    num = list(map(int, num))

    command = input()
    
    while command != 'end':
        command = command.split()
        
        if command[0] == 'first' or command[0] == 'last' and int(command[1] > len(num)):
            print ('Invalid count')
            continue
        
        if command[0] == 'exchange' and int(command[1]) < len(num):
            for x in range (int(command[1])):
                num.insert(0, num.pop())
        elif command[0] == 'max':
            if command [1] == 'even':
                print (num[num.index(max_even)])
            else:
                print (num[num.index(max_odd)])
        elif command[0] == 'min':
            if command[1] == 'even':
                print (num[num.index(min_even)])
            else:
                print (num[num.index(min_odd)])
        elif command[0] == 'first':
            index = int(command[1])
            if command[2] == 'even':
                print (list(even_nums[0:index]))
            else:
                print (list(odd_nums[0:index]))
        elif command[0] == 'last':
            index = int(command[1])
            if command[2] == 'even':
                even_nums.reverse()
                new_list_even = list(even_nums[0:index])
                new_list_even.reverse()
                print (new_list_even)
                even_nums.reverse()
            else:
                odd_nums.reverse()
                new_list_odd = list(odd_nums[0:index])
                new_list_odd.reverse()
                print (new_list_odd)
                odd_nums.reverse()
        command = input()

        
        
manipulator(numbers)