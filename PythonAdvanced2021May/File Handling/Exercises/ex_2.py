import re
import string
path = 'text.txt'


def counter(text_data):
    punctuation = list(string.punctuation)
    letters_found = len(re.findall(r'[A-Za-z]', text_data))
    punctuation_found = len([el for el in text_data if el in punctuation])
    return letters_found, punctuation_found


with open(path) as file:
    text = file.readlines()

new_text = []

for index in range(len(text)):
    letters, punctuations = counter(text[index])
    print(f'Line {index + 1}: {text[index].strip()} ({letters})({punctuations})')
    new_text.append(f'Line {index + 1}: {text[index].strip()} ({letters})({punctuations})\n')

with open('output', 'w') as new_file:
    new_file.writelines(new_text)


