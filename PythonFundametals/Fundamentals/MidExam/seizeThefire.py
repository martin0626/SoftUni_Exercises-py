fires = input().split('#')
water = int(input())
range_high = range(81, 126)
range_medium = range(51, 81)
range_low = range(1, 51)
effort = 0
cells = []
print ('Cells:')
for fire in fires:
    type_of_fire, value = fire.split(' = ')
    value = int(value)
    if type_of_fire == 'High' and value in range_high and water >= value:
        water -= value
        effort += 0.25 * value
        cells.append(value)
        print (f' - {value}')

    elif type_of_fire == 'Medium' and value in range_medium and water >= value:
        water -= value
        effort += 0.25 * value
        cells.append(value)
        print (f' - {value}')

    elif type_of_fire == 'Low' and value in range_low and water >= value:
        water -= value
        effort += 0.25 * value
        cells.append(value)
        print (f' - {value}')


# print ('\n - '.join(list(map(str, cells))))
print (f'Effort: {effort:.2f}\nTotal Fire: {sum(cells)}')


