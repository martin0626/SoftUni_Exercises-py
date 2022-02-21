mylist = [1, 2, 3, 4, 5, 6, 7, 10]

newlist = list(map(lambda a:(a % 3 == 0), mylist))
print (newlist)