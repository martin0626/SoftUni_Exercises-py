# words = input().split()
# palindroms = []
# word_needed = input()
# counter = 0
# for word in words:
#     if word == ''.join(reversed(word)):
#         palindroms.append(word)
#         if word_needed == word:
#             counter += 1
# print (f'{palindroms}\nFound palindrome {counter} times')
    

word = [word for word in input().split() if word == word[::-1]]
word_search = input()
print (f'Found palindrome {word.count(word_search)} times')
