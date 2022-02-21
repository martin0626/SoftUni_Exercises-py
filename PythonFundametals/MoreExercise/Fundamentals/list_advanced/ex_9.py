neighborhood = [int(num) for num in input().split('@')]
jumps = input()
index_now = 0
while not jumps == 'Love!':
    lenght = int(jumps.split()[1])
    index_now += lenght
    
    if index_now > (len(neighborhood) - 1):
        index_now = 0
    if neighborhood[index_now] != 0:  
        neighborhood[index_now] -= 2
        if neighborhood[index_now] == 0:
            print (f"Place {index_now} has Valentine's day.")
    else:
        print (f"Place {index_now} already had Valentine's day.")
    jumps = input()
neighborhood = [num for num in neighborhood if num != 0]
print (f"Cupid's last position was {index_now}.")

if len(neighborhood) > 0:
    print (f'Cupid has failed {len(neighborhood)} places.')

else:
    print ("Mission was successful.")
