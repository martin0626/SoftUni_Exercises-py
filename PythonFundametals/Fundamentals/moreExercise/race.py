import re
names = input().split(', ')
winners = {}
data = input()
while data != 'end of race':
    name = ''
    result_nums = 0
    for letter in data:
        letter_match = re.match('[A-Za-z]', letter)
        nums = re.match('\\d', letter)
        if letter_match:
            name += str(letter_match.group())
        elif nums:
            result_nums += int(nums.group())
    if name not in winners and name in names:
        winners[name] = result_nums
    elif name in winners and name in names:
         winners[name] += result_nums

    data = input()

winners = dict(sorted(winners.items(), key=lambda item: -item[1]))
counter = 1

for key in winners.keys():
    if counter == 1:
        print (f'1st place: {key}')
    elif counter == 2:
        print (f'2nd place: {key}')

    else:
        print (f'3rd place: {key}')
        break
    counter  += 1



