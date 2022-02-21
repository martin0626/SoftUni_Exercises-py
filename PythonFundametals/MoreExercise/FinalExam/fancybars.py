import re
barcodes = []
num = int(input())
pattern = r'(^|(?<=\s))@#+[A-Z][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9]+[A-Z]@#+'
for x in range (num):
    barcode = input()
    check = re.match(pattern, barcode)
    if check:
        result = [x for x in check.group() if x.isdigit()]
        if len(result) > 0:
            print (f'Product group: {"".join(result)}')
        else:
            print (f'Product group: 00')

    else:
        print ('Invalid barcode')
        

        

