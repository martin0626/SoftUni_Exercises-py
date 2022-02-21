digits = input()
def even_odd (numbers):
    even = 0
    odd = 0
    for x in numbers:
        number = int(x)
        if number % 2 == 0:
            even += number
        else:
            odd += number
    print (f'Odd sum = {odd}, Even sum = {even}')
even_odd(digits)
        
