num_joinery = int(input())
type_joinery = input()
delivery = input()
price = 0

if num_joinery >= 10:
    

    if type_joinery == '90X130':
        price = 110
        if num_joinery > 60:
            price -= price * 0.08
        elif num_joinery > 30: 
            price -= price * 0.05

    elif type_joinery == '100X150':
        price = 140
        if num_joinery > 80:
            price -= price * 0.1
        elif num_joinery > 40: 
            price -= price * 0.06

    elif type_joinery == '130X180':
        price = 190 
        if num_joinery > 50:
            price -= price * 0.12
        elif num_joinery > 20: 
            price -= price * 0.07

    elif type_joinery == '200X300':
        price = 250
        if num_joinery > 50:
            price -= price * 0.14
        elif num_joinery > 25: 
            price -= price * 0.09
    
else:
    print ('Invalid order')

total_price = price * num_joinery

if delivery == 'With delivery':
    total_price += 60


if num_joinery > 99:
    total_price -= total_price * 0.04

if num_joinery >= 10:
    print (f'{total_price:.2f} BGN')