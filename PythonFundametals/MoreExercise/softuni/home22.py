width_free = int(input())
lenght_free = int(input())
height_free = int(input())
free_space = width_free * lenght_free * height_free
space_left = 0
boxes = 0
while boxes <= free_space:
    box = input()
    if box == 'Done':
        space_left = free_space - boxes
        print (f'{space_left} Cubic meters left.')
        break
    box = int(box)  
    boxes += box
 
if free_space <= boxes:
    n = boxes - free_space
    print (f'No more free space! You need {n} Cubic meters more.')