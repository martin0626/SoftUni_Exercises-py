stack = [n for n in input().split()]

for _ in range(len(stack)):
    number = stack.pop()
    print(number, end=' ')
