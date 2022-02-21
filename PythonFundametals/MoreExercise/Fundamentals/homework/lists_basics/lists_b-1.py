head = input()
body = input()
tail = input()
list_1 = [head, body, tail]
list_1[0], list_1[2] = list_1[2], list_1[0]

print (list_1)