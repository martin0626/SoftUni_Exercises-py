string = input()
result = ''
for x in string:
    index = string.index(x)
    
    if index < (len(string) - 1):
        if x != string[index + 1]:
            result += x
            string = string.replace(x, '', 1)
        else:
            string = string.replace(x, '', 1)
    elif index == (len(string) - 1):
        result += x

print (''.join(result))
