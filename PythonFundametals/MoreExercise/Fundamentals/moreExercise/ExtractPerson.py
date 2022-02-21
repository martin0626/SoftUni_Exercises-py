n = int(input())

def find_name(text):
    name = ''
    for index in range(len(text)):
        if text[index] == '@':
            while text[index] != '|':
                if text[index] != '@':
                    name += text[index]
                index += 1
            return name

def find_age(text):
    age = ''
    for index in range(len(text)):
        if text[index] == '#':
            while text[index] != '*':
                if text[index] != '#':
                    age += text[index]
                index += 1
            return age




for _ in range (n):
    text = input()
    name = find_name(text)
    age = find_age(text)
    print (f"{name} is {age} years old.")

   
   
