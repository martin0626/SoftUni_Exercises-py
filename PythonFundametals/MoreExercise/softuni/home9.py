city = input ()
price = float(input())
commission = 0
error = False 
end_sum = 0
if city == 'Sofia':
    if 0 <= price <= 500:
        commission = 0.05
    elif 500 < price <= 1000:
        commission = 0.07
    elif 1000 < price <= 10000:
        commission = 0.08
    elif 10000 < price:
        commission = 0.12

    else:
        print ('error')
        error = True

elif city == 'Varna':
    if 0 <= price <= 500:
        commission = 0.045
    elif 500 < price <= 1000:
        commission = 0.075
    elif 1000 < price <= 10000:
        commission = 0.1
    elif 10000 < price:
        commission = 0.13
    else:
        print ('error')
        error = True
elif city == 'Plovdiv':
    if 0 <= price <= 500:
        commission = 0.055
    elif 500 < price <= 1000:
        commission = 0.08
    elif 1000 < price <= 10000:
        commission = 0.12
    elif 10000 < price:
        commission = 0.145
    else:
        print ('error')
        error = True

else:
    print ('error')
    error = True

if error == False:
    end_sum = commission * price
    print (f'{end_sum:.2f}')
    
