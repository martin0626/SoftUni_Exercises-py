def palindrome(word, index, current_word=''):
    index -= 1
    if len(word) == len(current_word):
        if current_word == word:
            return f'{word} is a palindrome'
        else:
            return f'{word} is not a palindrome'

    return palindrome(word, index, current_word + word[index])


print(palindrome("abcba", 0))
