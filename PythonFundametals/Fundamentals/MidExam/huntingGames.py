days = int(input())
players = int(input())
energy = float(input())
water_per_person = float(input())
food_per_person = float(input())
food_total = days * players * food_per_person
water_total = days * players * water_per_person

for day in range (1, days + 1):
    energy_lose = float(input())
    energy -= energy_lose
    if energy <= 0:
        print (f'You will run out of energy. You will be left with {food_total:.2f} food and {water_total:.2f} water.')
        break
    if day % 2 == 0:
        water_total -= 0.3 * water_total
        energy += 0.05 * energy

    if day % 3 == 0:
        food_total -= food_total / players
        energy += energy * 0.1

if energy > 0:
    print (f'You are ready for the quest. You will be left with - {energy:.2f} energy!')