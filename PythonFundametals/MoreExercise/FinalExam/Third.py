peter = {}
records = 0
command_data = input()

while command_data != 'Log out':
    command_data = command_data.split(': ')

    command = command_data[0]

    if command == 'New follower':
        username = command_data[1]
        if username not in peter:
            peter[username] = {'likes': 0, 'comments': 0, 'sum' : 0}

        
    elif command == 'Like':
        user = command_data[1]
        like_count = int(command_data[2])
        if user in peter:
            peter[user]['likes'] += like_count
        else:
            peter[user] = {'likes': 0, 'comments': 0, 'sum': 0}
            peter[user]['likes'] += like_count

    elif command == 'Comment':
        user_name = command_data[1]
        if user_name in peter:
            peter[user_name]['comments'] += 1
        else:
            peter[user_name] = {'likes': 0, 'comments': 0, 'sum': 0}
            peter[user_name]['comments'] += 1

            

 
    elif command == 'Blocked':
        user_to_del = command_data[1]
        if user_to_del in peter:
            del peter[user_to_del]

        else:
            print (f"{user_to_del} doesn't exist.")
    command_data = input()    

for key in peter.keys():
    peter[key]['sum'] = peter[key]['likes'] + peter[key]['comments']

peter = dict(sorted(peter.items(), key = lambda x: (-x[1]['sum'], x[0]))) 
print (f'{len(peter)} followers')
for key in peter.keys():
    print (f"{key}: {peter[key]['sum']}")


