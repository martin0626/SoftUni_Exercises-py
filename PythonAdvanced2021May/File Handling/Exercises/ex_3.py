import os


def create_file(name):
    with open(name, 'w') as file:
        return


def add_content(name, content_to_add):
    with open(name, 'a') as file:
        file.writelines(f'{content_to_add}\n')
    return


def replace(new_content, old_content, name):
    try:
        with open(name, 'r') as file:
            text = file.read()

        text = text.replace(old_content, new_content)

        with open(name, 'w') as file:
            file.write(text)

    except FileNotFoundError:
        print('An error occurred')
    return


def delete_file(name):
    try:
        os.remove(name)

    except FileNotFoundError:
        print(f'An error occurred')
    return


while True:
    cmd = input()

    if cmd == 'End':
        break

    command, file_name = cmd.split('-')[0:2]

    if command == 'Create':
        create_file(file_name)

    elif command == 'Add':
        content = cmd.split('-')[2]
        add_content(file_name, content)

    elif command == 'Replace':
        old_string, new_string = cmd.split('-')[2:]
        replace(new_string, old_string, file_name)

    elif command == 'Delete':
        delete_file(file_name)
