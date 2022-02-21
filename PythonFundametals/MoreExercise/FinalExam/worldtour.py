def add_stop (cities, index, string):
    if 0 <= index < len(cities):
        cities = cities[:index] + string + cities[index:]
    
    return cities

def remove_stop (cities, start_index, stop_index):
    if 0 <= start_index < len(cities) and 0 <= stop_index < len(cities):
        cities = cities[:start_index] + cities[stop_index + 1:]

    return cities

def switch(cities, old_string, new_string):
    if old_string in cities:
        cities = cities.replace(old_string, new_string)
    return cities



cities = input()

command = input()

while command != 'Travel':
    command = command.split(':')

    if command[0] == 'Add Stop':
        index = int(command[1])
        replacement = command[2]
        cities = add_stop(cities, index, replacement)
        


    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        stop_index = int(command[2])
        cities = remove_stop(cities, start_index, stop_index)
        
    else:
        old_string = command[1]
        new_string = command[2]
        cities = switch(cities, old_string, new_string)

    
    print (cities)
    command = input()
    
print (f'Ready for world tour! Planned stops: {cities}')