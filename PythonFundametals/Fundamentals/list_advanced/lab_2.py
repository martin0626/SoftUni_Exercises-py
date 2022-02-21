todo_list = [0] * 10
notes = input()
while not notes == 'End':
    importance, value = notes.split('-')
    todo_list.insert(int(importance), value)
    notes = input()

result = []
for x in todo_list:
    if x != 0:
        result.append(x)
print (result)