import random 
cards = input().split()
faro = int(input())

first = cards[0]
last = cards[-1]
cards.pop(-1)
cards.pop(0)

new_list = []

for x in cards:
    new_list.append(x)
    
random.seed(faro)
random.shuffle(new_list)
new_list.insert(0, first)
new_list.insert(len(new_list), last)

print (new_list)
