string = input()
n = int(input())

def repeat (s, x):
    result = ''
    for i in range (x):
        result += s
    return result
print(repeat(string, n))