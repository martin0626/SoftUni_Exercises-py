from collections import deque

queue = deque([n for n in input().split()])

turns = int(input())
current_turn = 0

while len(queue) > 1:

    current_player = queue.popleft()
    current_turn += 1

    if current_turn == turns:
        current_turn = 0
        print(f'Removed {current_player}')

    else:
        queue.append(current_player)

print(f'Last is {queue[0]}')
