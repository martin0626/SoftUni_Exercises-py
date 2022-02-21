num = int(input())
positive = []
negative = []
positive_sum = 0
negative_sum = 0
for x in range (num):
    number = int(input())
    if number >= 0:
        positive.append(number)
        positive_sum += 1
    else:
        negative.append(number)
        negative_sum += number
print (positive)
print (negative)
print (f'Count of positives: {positive_sum}. Sum of negatives: {negative_sum}')
