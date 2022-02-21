companies = {}

command = input()

while command != 'End':
    company, id_emp = command.split(' -> ')

    if company not in companies:
        companies[company] = []
    if id_emp not in companies[company]:
        companies[company].append(id_emp)
    command = input()



companies = dict(sorted(companies.items(), key=lambda item: item[0]))
for k, v in companies.items():
    print (k)
    for x in v:
        print ('--', x)