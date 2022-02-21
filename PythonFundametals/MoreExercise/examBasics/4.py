num_balls = int(input())
red = 0
orange = 0
yellow = 0
white = 0
black = 0
others = 0
total_sum = 0
for x in range (num_balls):
    colour = input()

    if colour == 'red':
        total_sum += 5
        red += 1
    elif colour == 'orange':
        total_sum += 10
        orange += 1
    elif colour == 'yellow':
        total_sum += 15
        yellow += 1
    elif colour == 'white':
        total_sum += 20
        white += 1
    elif colour == 'black':
        total_sum = total_sum // 2
        black += 1
    else:
        others += 1

print (f'Total points: {total_sum}\nPoints from red balls: {red}')
print (f'Points from orange balls: {orange}\nPoints from yellow balls: {yellow}')
print (f'Points from white balls: {white}\nOther colors picked: {others}')
print (f'Divides from black balls: {black}')