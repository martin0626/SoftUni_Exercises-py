numbers = list(map(int, input().split()))

positive = list(filter(lambda x: x > 0, numbers))
negative = list(filter(lambda x: x < 0, numbers))

print(sum(negative))
print(sum(positive))

if abs(sum(negative)) > abs(sum(positive)):
    print('The negatives are stronger than the positives')

else:
    print('The positives are stronger than the negatives')
