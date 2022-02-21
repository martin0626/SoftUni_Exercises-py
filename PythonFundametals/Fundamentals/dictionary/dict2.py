dic1={'1':10, '2':20}
dic2={'3':30, '4':40}
dic3={'5':50,'6':60}

sum_dict = {}
for x in (dic1, dic2, dic3):
    sum_dict.update(x)

print (sum_dict)