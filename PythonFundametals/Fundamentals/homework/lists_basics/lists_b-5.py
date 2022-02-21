numbers = input().split()
new_numbers = []
for num in numbers:
    num = int(num) * -1
    new_numbers.append(num)
print (new_numbers)