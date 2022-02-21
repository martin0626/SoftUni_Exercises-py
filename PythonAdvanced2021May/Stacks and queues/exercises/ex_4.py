clothes = [int(c) for c in input().split()]
capacity = int(input())
racks = 0
current_sum = 0

while clothes:

    current_clothe = clothes.pop()
    current_sum += current_clothe

    if current_sum == capacity:
        current_sum = 0
        racks += 1

    elif current_sum > capacity:
        clothes.append(current_clothe)
        racks += 1
        current_sum = 0

    elif not clothes:
        racks += 1


print(racks)
