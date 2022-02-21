import re


def print_result(dict_result: dict):
        [print(f'{w} - {n}') for w, n in dict_result.items()]
        return


with open('text.txt') as file:
    text = file.read()
with open('input.txt') as file:
    words_to_search = [el for el in file.readline().split()]

all_words = re.findall(r'[a-zA-Z\']+', text.lower())
dict_words = {word: all_words.count(word) for word in words_to_search}
result = dict(sorted(dict_words.items(), key=lambda kv: -kv[1]))
print_result(result)
