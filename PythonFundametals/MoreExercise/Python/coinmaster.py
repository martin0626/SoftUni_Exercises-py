a = float(input())
b = a * 100
coins = 0



while b > 0:
    if b >= 200:
        coins += 1
        b -= 200
    elif b >= 100:
        coins += 1
        b -= 100
    elif b >= 50:
        coins += 1
        b -= 50
    elif b >= 20:
        coins += 1
        b -= 20
    elif b >= 10:
        coins += 1
        b -= 10
    elif b >= 5:
        coins += 1
        b -= 5
    elif b >= 2:
        coins += 1
        b -= 2
    elif b >= 1:
        coins += 1
        b -= 1
    if b < 1:
        break
print (coins)


