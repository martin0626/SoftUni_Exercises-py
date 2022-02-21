import re

pattern = r'%(?P<name>[A-Z][a-z]+)%([A-Za-z0-9]+)?<(?P<product>[A-Za-z0-9]+)>([A-Za-z0-9]+)?\|(?P<count>[0-9]+)\|([A-Za-z]+)?(?P<price>[0-9]+\.?[0-9]*)\$([A-Za-z0-9]+)?'

data = input()
data_list = ''

while data != 'end of shift':
    data_list += " " + data

    data = input()

result = re.finditer(pattern, data_list)

total = 0
for x in result:
    x = x.groupdict()
    sum_price = int(x['count']) * float(x['price'])
    total += sum_price
    print (f'{x["name"]}: {x["product"]} - {sum_price:.2f}')
print (f'Total income: {total:.2f}')

