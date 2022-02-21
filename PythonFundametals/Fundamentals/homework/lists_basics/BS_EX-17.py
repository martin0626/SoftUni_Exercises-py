import math
party_size = int(input())
days = int(input())
money_earn = 0
for day in range(1, days + 1):
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    money_earn += 50
    money_earn -= 2 * party_size
    if day % 3 == 0:
        money_earn -= 3 * party_size
    if day % 5 == 0:
        money_earn += 20 * party_size
        if day % 3 == 0:
            money_earn -= 2 * party_size
money_for_each = math.floor(money_earn / party_size)
print (f'{party_size} companions received {money_for_each} coins each.')