x = float(input())
y = float(input())
h = float(input())
door = 1.2 * 2
window = 1.5 * 1.5
side_walls = ((x * y) * 2) - window * 2
front_walls = (x * x) * 2 - door
ceilling = ((x * h) / 2) * 2 + (x * y) * 2

red_colour = ceilling / 4.3
green_colour = (side_walls + front_walls) / 3.4

print (f'{green_colour:.1f}')
print (f'{red_colour:.1f}')