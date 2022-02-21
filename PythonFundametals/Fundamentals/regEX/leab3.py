import re

text = input()

pattern = r'(?P<day>\d{2})(?P<sep>[\./-])(?P<mounth>[A-Z][a-z]{2})(?P=sep)(?P<year>\d{4})'

result = re.finditer(pattern, text)

for day in result:
    x = day.groupdict()
    print (f"Day: {x['day']}, Month: {x['mounth']}, Year: {x['year']}")