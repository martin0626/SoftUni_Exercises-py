import re
text = input()
searched = input()

result = re.findall(f"\\b{searched}\\b", text, re.IGNORECASE)


print (len(result))
