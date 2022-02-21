stack = []

n = int(input())

for _ in range(n):
    command = input()

    if command == '2':
        try:
            stack.pop()
        except IndexError:
            pass

    elif command == '3' and stack:
        print(max(stack))

    elif command == '4' and stack:
        print(min(stack))

    elif command.split()[0] == '1':
        num_to_add = command.split()[1]
        stack.append(int(num_to_add))

elements = ', '.join([str(el) for el in reversed(stack)])

print(elements)
