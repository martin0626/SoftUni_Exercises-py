text = input()


final_result = ''
current_text = ''


index = 0
while index < len(text):

    if not text[index].isdigit():
        current_text += text[index]
        index += 1
    else:
        number = ''
        while index < len(text) and text[index].isdigit():
            number += text[index]
            index += 1
        number = int(number)
        final_result += current_text.upper() * number
        current_text = ''




print (f'Unique symbols used: {len(set(final_result))}')
print (final_result)

    

     
