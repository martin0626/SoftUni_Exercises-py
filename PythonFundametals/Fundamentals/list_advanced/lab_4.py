# numbers =list(map(lambda x: int(x), input().split(', ')))
# indexes = []
# for num in range (len(numbers)):
#     if numbers[num] % 2 == 0:
#         indexes.append(num)
# print (indexes)


numbers = [int(num) for num in input().split()]
even = [index for index in range (len(numbers)) if numbers[index] % 2 == 0]
print (even)
