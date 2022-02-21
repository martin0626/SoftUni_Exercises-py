import os


files = list(*next(os.walk(input()))[2:])
extensions = {}

for file in files:
    extension = file.split('.')[-1]

    if extension not in extensions:
        extensions[extension] = []
    extensions[extension].append(file)

with open(os.path.expanduser(r'~\Desktop\result.txt'), 'w') as result_file:
    for ex in sorted(extensions.keys()):
        result_file.write(f'.{ex}\n')
        for file in sorted(extensions[ex]):
            result_file.write(f'- - - {file}\n')

