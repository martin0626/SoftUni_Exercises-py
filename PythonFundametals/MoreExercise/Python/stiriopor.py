import math
budget = float(input())
size = float(input())
windows_num = int(input())
pacet_styr = float(input())
price_one = float(input())


windows_in_house = 2.4 * windows_num
size -= windows_in_house 
size += size * 0.1
packet_needed = size / pacet_styr
packet_needed = math.ceil(packet_needed)
finall_price = packet_needed * price_one

if budget >= finall_price:
    print (f'Spent: {finall_price}')
    print (f'Left: {budget - finall_price}')
else:
    print (f'Need mor: {finall_price}')



