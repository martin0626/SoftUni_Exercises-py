n = int(input())

def top_print (num):
    print ('-' * (2 * num))

def body_print (num):
    
    for x in range (1, num - 1):
        print ('-' + '\\/' * int((2 * num - 2) / 2) + '-')
top_print(n)
body_print(n)
top_print(n)
