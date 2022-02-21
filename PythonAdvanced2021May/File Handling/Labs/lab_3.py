text = input()

with open('my_first_file.txt', 'a') as file:
    file.writelines(f'\n{text}')
