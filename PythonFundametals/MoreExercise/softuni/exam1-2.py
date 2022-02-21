wiskey = float(input())
beer_l = float(input())
wine_l = float(input())
rakiq_l = float(input())
wiskey_l = float(input())

rakiq_price = wiskey / 2
wine_price = rakiq_price - (rakiq_price * 0.4) 
beer_price = rakiq_price - (rakiq_price * 0.8)

wiskey_sum = wiskey * wiskey_l
rakiq_sum = rakiq_l * rakiq_price
wine_sum = wine_price * wine_l
beer_sum = beer_l * beer_price

sum_all = wiskey_sum + rakiq_sum + wine_sum + beer_sum


print (f'{sum_all:.2f}')
