strings = input().split()

string_1 = strings[0]
string_2 = strings[1]
lenght = None

if len(string_1) <= len(string_2):
    lenght = len(string_1)
    if len(string_2) > len(string_1):
        longer = string_2
    else:
        longer = 0
else:
    lenght = len(string_2)
    longer = string_1


sum_strings = 0

for index in range (0, lenght):
    sum_strings += ord(string_1[index]) * ord(string_2[index])

if longer != 0:
    for rest in range (lenght, len(longer)):
        sum_strings += ord(longer[rest])

print (sum_strings)