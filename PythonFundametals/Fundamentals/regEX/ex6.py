import re

emails = input()
all_emails = []
while emails != '':
    all_emails.append(emails)
    emails = input()

pattern = r'(^|(?<=\s))w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+($|\s)'
all_emails = ' '.join(all_emails)
results = re.finditer(pattern, all_emails)

results = [x.group() for x in results]

for result in results:
    print (result)