word = input()
reverse = ""
for x in range (len(word) - 1, - 1, -1):
    reverse += word[x]
print (reverse)