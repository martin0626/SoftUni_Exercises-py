num_electrons = int(input())
electrons = []
current_index = 1

while num_electrons > 0:
    possible_electrons = 2 * current_index**2
    if possible_electrons > num_electrons:
        electrons.append(num_electrons)
    else:
        electrons.append(possible_electrons)
    num_electrons -= possible_electrons
    current_index += 1

print (electrons)