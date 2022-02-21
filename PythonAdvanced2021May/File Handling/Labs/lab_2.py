with open('text.txt', 'r') as file:
    result = 0
    for line in file.readlines():
        result += int(line)
        print(int(line))

print(result)
