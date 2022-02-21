num = int(input())
even = []
odd = []
negative = []
positive = []

for x in range (num):
    number = int(input())
    if number % 2 == 0:
        even.append(number)
    if number % 2 != 0:
        odd.append(number)
    if number < 0:
        negative.append(number)
    if number >= 0:
        positive.append(number)

type = input()
if type == 'even':
    print (even)
elif type == 'odd':
    print(odd)
elif type == 'negative':
    print(negative)
else:
    print (positive)