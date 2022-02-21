start_char = input()
end_char = input()

def in_range (start, finish):
    characters = []
    for char in range (ord(start) + 1, ord(finish)):
        characters.append(chr(char))
    return characters
print (*in_range(start_char, end_char))