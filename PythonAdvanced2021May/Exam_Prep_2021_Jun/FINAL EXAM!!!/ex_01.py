from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milks = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while chocolates and milks:

    chocolate = chocolates.pop()
    milk = milks.popleft()

    if chocolate <= 0 or milk <= 0:
        if chocolate > 0:
            chocolates.append(chocolate)
        if milk > 0:
            milks.appendleft(milk)
        continue

    if milk == chocolate:
        milkshakes += 1

    elif milk != chocolate:
        chocolate -= 5
        milks.append(milk)
        if chocolate > 0:
            chocolates.append(chocolate)

    if milkshakes >= 5:
        print('Great! You made all the chocolate milkshakes needed!')
        break

if milkshakes < 5:
    print('Not enough milkshakes.')

if chocolates:
    print(f'Chocolate: {", ".join([str(c) for c in chocolates])}')

else:
    print('Chocolate: empty')

if milks:
    print(f'Milk: {", ".join([str(m) for m in milks])}')

else:
    print('Milk: empty')