text = input()
nums = range(48, 58)
letters_lower = range(97, 123)
letters_upper = range(65, 91)
symbols = range(33, 48)
result = {'numbers':'', 'letters':'', 'symbol':''}
for digit in text:
    if ord(digit) in nums:
        result['numbers'] += digit
    elif ord(digit) in letters_lower or ord(digit) in letters_upper:
        result['letters']+= digit
    else:
        result['symbol'] += digit

for value in result.values():
    print (value)

    
    
