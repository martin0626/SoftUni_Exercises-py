from collections import deque

food_quantity = int(input())
clients = deque([int(c) for c in input().split()])

best_client = max(clients)

print(best_client)

for _ in range(len(clients)):
    current_client = clients.popleft()

    if current_client <= food_quantity:
        food_quantity -= current_client

    else:
        clients.appendleft(current_client)
        break

if clients:
    all_clients = ' '.join([str(c) for c in clients])
    print(f'Orders left: {all_clients}')

else:
    print('Orders complete')
