a = input()

sum_prime = 0
sum_non = 0

while a != 'stop':
    non_prime = True 
    a = int(a)
    if a < 0:
        print ('Number is negative.')
    
    if a <= 1: 
        non_prime = False
    for i in range (2, a):
        if (a % i == 0):
            non_prime = False

    if non_prime and a > 0:
        sum_non += a
    elif non_prime == False and a > 0: 
        sum_prime += a

    a = input()
print (f'Sum of all prime numbers is: {sum_non}')
print (f'Sum of all non prime numbers is: {sum_prime}')



