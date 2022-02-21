numbers = [int(num) for num in input().split()]
command = input()
result = []
while  command != 'End':
    action, index, data_int = command.split()
    index = int(index)
    data_int = int(data_int)

    if action == 'Shoot':
        if index <= len(numbers) - 1 and index >= 0:
            numbers[index] -= data_int
        

    elif action == 'Add':
        if 0 <= index <= len(numbers):
            numbers.insert(index, data_int)
        else:
            print ('Invalid placement!')
    elif action == 'Strike':
        if  (index + data_int) <= (len(numbers) - 1) and (index - data_int) >= 0:
            for x in range (index - data_int, (index + data_int) + 1):
                numbers[x] = 0
        else:
            print ('Strike missed!')
    
    command = input()
    numbers = [num for num in numbers if not num <= 0]  
numbers = list(map(str, numbers))
print ('|'.join(numbers))
  

            


