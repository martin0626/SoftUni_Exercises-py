import re
text = input()

pattern = r'([=/])(?P<destination>[A-Z][A-Za-z]{2,})\1'
result = re.finditer(pattern, text)

destinations_list = []
travel_points = 0
for destination in result:
    destination = destination.groupdict()
    travel_points += len(destination['destination'])
    destinations_list.append(destination['destination'])

print (f"Destinations: {', '.join(destinations_list)}\nTravel Points: {travel_points}")

