num = int(input())
word = input()
list_all = []
list_word = []


for x in range (num):
    sentences = input()
    list_all.append(sentences)
    if word in sentences:
        list_word.append(sentences)
print(f'{list_all}\n{list_word}')