import re


text = input()
pattern = r'([#|])(?P<name>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d{1,5})\1'
result = re.finditer(pattern, text)

calories_sum = 0
result_strings = []
for item in result:
    item = item.groupdict()
    calories_sum += int(item['calories'])
    string = f'Item: {item["name"]}, Best before: {item["date"]}, Nutrition: {item["calories"]}'
    result_strings.append(string)




days = calories_sum // 2000
print (f'You have food to last you for: {days} days!')
print ('\n'.join(result_strings))





