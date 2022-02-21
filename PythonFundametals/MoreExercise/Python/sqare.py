n = int(input())

def top_print (num):
    print ('-' * (num * 2) )

def middle_print (number):
    for i in range (1, number - 1):
        print ('-' + '\\/' * int((2*number - 2)/2) + '-')

top_print(n)
middle_print(n)
top_print(n)