import re
n = int(input())
star = ['s', 't', 'a', 'r']
crypted = {}


for _ in range (n):
    data = input()
    num = len([digit for digit in data if digit.lower() in star])
    
    crypted[data] = num 

result = ''
for key in crypted.keys():
    
    for digit in key:
        result += chr(ord(digit) - crypted[key])
    result += ' '

pattern = r'@(?P<planet>[A-Za-z]+)([A-Za-z0-9])?:(?P<population>[0-9]+)!(?P<type>[AD])!([A-Za-z0-9])?->(?P<soldiers>[0-9]+)'

result_search = re.finditer(pattern, result)
atacked = [] 
destroed = []
for x in result_search:
    x = x.groupdict()
    if x['type'] == 'A':
        atacked.append(x['planet'])
    else:
        destroed.append(x['planet'])
    
print (f'Attacked planets:\n{len(atacked)}')

print (f'Destroyed planets:\n{len(destroed)}')




    
    


