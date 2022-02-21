title = input()
content = input()
comment = input()
comments_list = []
while comment != 'end of comments':
    comments_list.append(comment)
    comment = input()


print (f'<h1>\n   {title}\n</h1>')
print (f'<article>\n   {content}\n</article>')

for com in comments_list:
    print (f'<div>\n   {com}\n</div>')