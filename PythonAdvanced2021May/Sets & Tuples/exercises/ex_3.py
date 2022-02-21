def unpack(elements_list, set_to_add):
    for el in elements_list:
        set_to_add.add(el)

    return set_to_add


n = int(input())
unique_el = set()

for _ in range(n):
    elements = input().split()
    unique_el = unpack(elements, unique_el)

[print(el) for el in unique_el]
