from fibonacci_seq import fib, is_number_in
current_seq = []

while True:
    command = input()

    if command == 'Stop':
        break

    if command.startswith('Create'):
        length = int(command.split()[-1])
        current_seq = fib(length)
        print(*current_seq)

    elif command.startswith('Locate'):
        number = int(command.split()[-1])
        print(is_number_in(number, current_seq))
