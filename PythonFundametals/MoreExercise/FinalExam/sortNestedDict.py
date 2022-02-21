from collections import OrderedDict 
from operator import getitem

items = {'Marto':{'hp': 122}, 'Ivan':{'hp': 11}, 'Ani':{'hp': 222}, 'Adal':{'hp': 122}}

items = dict(OrderedDict(sorted(items.items(), key = lambda x: (-getitem(x[1], 'hp'), x[0]))))

print (items)