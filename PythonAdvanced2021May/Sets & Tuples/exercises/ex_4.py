text = ([el for el in input()])

elements = {}

for symbol in text:

    if symbol not in elements:
        elements[symbol] = text.count(symbol)

elements = dict(sorted(elements.items(), key=lambda kv: kv[0]))

for el in elements:
    print(f'{el}: {elements[el]} time/s')
