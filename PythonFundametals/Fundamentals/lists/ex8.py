stats = input().split('#')
water = int(input())
effort = 0
total_fire = 0

cell_list = []
print('Cells:')
for cell in stats:
    fire_cells = cell.split(' = ')
    type_fire = fire_cells[0]
    range1 = int(fire_cells[1])

    if type_fire == 'High' and 81 <= range1 <= 125 and range1 <= water:
        print ('-' ,range1)
        water -= range1
        total_fire += range1
        effort += 0.25 * range1
    elif type_fire == 'Medium' and 51 <= range1 <= 80 and water >= range1:
        print ('-' ,range1)
        water -= range1
        total_fire += range1
        effort += 0.25 * range1
    elif type_fire == 'Low' and 1 <= range1 <= 50 and water >= range1:
        print ('-' ,range1)
        water -= range1
        total_fire += range1
        effort += 0.25 * range1
    else:
        continue
print (f'Effort: {effort:.2f}\nTotal Fire: {total_fire:}')





