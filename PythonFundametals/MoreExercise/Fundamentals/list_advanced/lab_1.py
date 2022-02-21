wagons = int(input())
def list_of_zeroes (num):
    l = [0] * num
    return l
list_wagons = list_of_zeroes(wagons)
command = input()
while not command == 'End':
    command = command.split()

    if command[0] == 'add':
        list_wagons[-1] += int(command[1])
    elif command[0] == 'insert':
        list_wagons[int(command[1])] += int(command[2])
    elif command[0] == 'leave':
        list_wagons[int(command[1])] -= int(command[2])
    command = input()
print (list_wagons)