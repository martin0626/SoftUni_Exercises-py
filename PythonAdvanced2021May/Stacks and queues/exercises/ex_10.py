from collections import deque

cups = deque([int(c) for c in input().split()])
bottles = [int(b) for b in input().split()]

wasted_water = 0

while cups and bottles:
    cup = cups.popleft()
    bottle = bottles.pop()

    if bottle >= cup:
        wasted_water += bottle - cup

    else:
        cup -= bottle
        cups.appendleft(cup)

if cups:
    remaining_cups = " ".join([str(c) for c in cups])
    print(f'Cups: {remaining_cups}')

else:
    remaining_bottles = ' '.join([str(b) for b in reversed(bottles)])
    print(f'Bottles: {remaining_bottles}')

print(f'Wasted litters of water: {wasted_water}')
