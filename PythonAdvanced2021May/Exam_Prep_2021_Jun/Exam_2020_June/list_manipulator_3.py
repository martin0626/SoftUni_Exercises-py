from collections import deque


def list_manipulator(list_manipulate, command, place, *args):
    list_manipulate = deque(list_manipulate)
    if command == 'add':
        if place == 'beginning':
            list_manipulate.extendleft(reversed(args))

        elif place == 'end':
            list_manipulate.extend(args)

    elif command == 'remove':
        if place == 'beginning':
            if args:
                for _ in range(args[0]):
                    list_manipulate.popleft()

            elif not args:
                list_manipulate.popleft()

        elif place == 'end':
            if args:
                for _ in range(args[0]):
                    list_manipulate.pop()

            elif not args:
                list_manipulate.pop()

    return list(list_manipulate)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
