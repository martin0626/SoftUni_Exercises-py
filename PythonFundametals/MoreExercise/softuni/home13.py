n1 = int(input())
n2 = int(input())
operation = input()
result = 0
even_odd = ''
if operation == '+':
    result = n1 + n2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    print (f'{n1} {operation} {n2} = {result} – {even_odd}')
elif operation == '-':
    result = n1 - n2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    print (f'{n1} {operation} {n2} = {result} – {even_odd}')
    
    
elif operation == '*':
    result = n1 * n2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    print (f'{n1} {operation} {n2} = {result} – {even_odd}')

elif n2 != 0:
    if operation == '/':
        result = n1 / n2
        print (f'{n1} {operation} {n2} = {result}')


    elif operation == '%':
        result = n1 % n2
        print (f'{n1} {operation} {n2} = {result}')
elif n2 == 0:
    print (f'Cannot divide {n1} by zero')
            

 



