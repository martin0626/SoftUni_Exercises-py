string_for_decipher = input().split()
ascii_numbers = range (48, 58)
all_words = []
new_word = ''
for word in string_for_decipher:
    
    number = ''
    for x in word:
        if ord(x) in ascii_numbers:
            number += x
   
    
    new_word = word.replace(str(number), '')
    new_word = chr(int(number)) + new_word
    if not len(new_word) == 2: 
        new_word = new_word[0:1] + new_word[-1] + new_word[2:-1] + new_word[1]
    
    all_words.append(new_word)

print (*all_words)
    
    