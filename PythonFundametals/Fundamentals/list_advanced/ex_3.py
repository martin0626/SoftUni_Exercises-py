version = input().split('.')


    
first = version[0]
second = version[1]
third = version[2]

if int(third) == 9:
    third = '0'
    second = str(int(second) + 1)
    if int(second) > 9:
        second = '0'
        first = str(int(first) + 1)
else:
    third = str(int(third) + 1)

result = []

result.append(first)
result.append(second)
result.append(third)
print ('.'.join(result))

