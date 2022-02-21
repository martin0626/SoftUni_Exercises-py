from collections import deque

queue = deque([])
quantity = int(input())

while True:

    command = input()

    if command == 'Start':
        break

    queue.append(command)


while True:

    command = input()

    if command == 'End':
        print(f'{quantity} liters left')
        break

    try:
        litters_to_refill = int(command.split()[1])
        quantity += litters_to_refill

    except IndexError:
        letters = int(command)
        if quantity >= letters:
            quantity -= letters
            person = queue.popleft()
            print(f'{person} got water')
        else:
            person = queue.popleft()
            print(f'{person} must wait')
