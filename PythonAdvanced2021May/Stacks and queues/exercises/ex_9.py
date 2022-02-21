from collections import deque


bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(b) for b in input().split()]
locks = deque([int(l) for l in input().split()])
intelligence = int(input())
bullet_shoot = 0

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    bullet_shoot += 1
    intelligence -= bullet_price

    if current_bullet <= current_lock:
        print('Bang!')

    else:
        print('Ping!')
        locks.appendleft(current_lock)

    if bullet_shoot == gun_barrel_size and bullets:
        print('Reloading!')
        bullet_shoot = 0

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f'{len(bullets)} bullets left. Earned ${intelligence}')
