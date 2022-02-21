n = int(input())

def num (number):
    if number > 0:
        print (f'The number {number} is positive.')
    elif number < 0:
        print (f'The number {number} is negative.')
    else:
        print ('The number 0 is zero.')

num(n)