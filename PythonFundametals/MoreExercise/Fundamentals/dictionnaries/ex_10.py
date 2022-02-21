command = input()

user_lang = {}
user_point = {}

while command != 'exam finished':
    
    command = command.split('-')
    
    if command[1] == 'banned':
        name = command[0]
        if name in user_point.keys(): 
            del user_point[name]

    else:
        name, lang, points = command
        points = int(points)
        if lang not in user_lang:
            user_lang[lang] = 0
        user_lang[lang] += 1

        if name not in user_point:
            user_point[name] = points
        elif user_point[name] < points:
            user_point[name] = points

    command = input()

user_point = dict(sorted(user_point.items(), key=lambda item: (-item[1], item[0])))

print ('Results:')
for key, value in user_point.items():
    print (f'{key} | {value}')
print('Submissions:')

user_lang = dict(sorted(user_lang.items(), key=lambda item: (-item[1], item[0])))

key, value in user_lang.items():
    print (f'{key} - {value}')



        




    








