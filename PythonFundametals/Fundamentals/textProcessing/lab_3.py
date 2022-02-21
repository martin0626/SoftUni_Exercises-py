string = input()
second_string = input()


while True:

    if string in second_string:
        second_string = second_string.replace(string, '')
    else:
        break
print (second_string)

