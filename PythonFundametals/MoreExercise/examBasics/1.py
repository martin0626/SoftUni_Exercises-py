company_name = input()
adult_tickets = int(input())
kid_tickets = int(input())
adult_price = float(input())
fee = float(input())


adult_sum = (adult_price + fee) * adult_tickets
kid_price = adult_price - (adult_price *  0.7)
kid_sum = (kid_price + fee) * kid_tickets

total_sum = adult_sum + kid_sum
profit = total_sum * 0.2

print (f'The profit of your agency from {company_name} tickets is {profit:.2f} lv.')
