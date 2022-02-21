from collections import deque


def empty_queue(queue_to_empty):
    for _ in range(len(queue_to_empty)):
        customer = queue_to_empty.popleft()
        print(customer)
    return queue


queue = deque([])

while True:
    
    command = input()

    if command == 'End':
        print(f'{len(queue)} people remaining.')
        break

    elif command == 'Paid':
        queue = empty_queue(queue)

    else:
        queue.append(command)
