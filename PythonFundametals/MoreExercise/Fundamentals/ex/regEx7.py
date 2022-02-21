import re

pattern = r'\b359(-|\s)\w{1}(-|\s)\w{3}(-|\s)\w{4}\b'
text = input()

result = re.findall(pattern, text)
if re.search(pattern,text):
    print("Valid phone number")
else:
    print("Invalid phone number")

