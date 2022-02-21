import math
century = int(input())
years = century * 100
days = math.floor(years * 365.2422)
hours = math.floor(days * 24)
minutes = math.floor(hours * 60)

print (f'{century} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')
