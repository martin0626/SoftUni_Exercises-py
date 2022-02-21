import re

text_to_search = '''
dasdasdascas
ABCDEFGHIJKLMOPQRSTUVWXYZ
1234567890
Ha HaHa

martin.com

321-555-4321
123.555.1234
3456.666.4532

Mr. Schafer 
Mr Smith
Ms Davis
Mrs Robinson
 '''
sentence = 'Start of the end'
#pattern = re.compile(r'\d+.\d{3}.\d{4}')
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Za-z]*')
matches = pattern.finditer(text_to_search)

for match in matches:
    print (match)