expression = input()

stack = []

for i in range(len(expression)):
    if expression[i] == '(':
        stack.append(i)

    elif expression[i] == ')':
        start_index = stack.pop()
        print(expression[start_index:i + 1])
