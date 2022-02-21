text = input().split(', ')
valid_usernames = []


def is_valid (username):
    if 3 < len(username) < 16:
        validation_num = 0
        for digit in username:
            if digit.isdigit() or digit == '-' or digit == '_' or digit.isalpha():
                validation_num += 1
        if validation_num == len(username):
            return username


for username in text:
    if is_valid(username) != None:
        valid_usernames.append(is_valid(username))

print ('\n'.join(valid_usernames))