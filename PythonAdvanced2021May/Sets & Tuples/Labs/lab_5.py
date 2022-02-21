n = int(input())
reservations = set([input() for _ in range(n)])
guests_came = set()

while True:

    guest = input()

    if guest == 'END':
        break

    if guest in reservations:
        guests_came.add(guest)

people_missing = reservations.difference(guests_came)

print(len(people_missing))
[print(g) for g in sorted(list(people_missing)) if isinstance(g[0], int)]
[print(g) for g in sorted(list(people_missing)) if not isinstance(g[0], int)]
