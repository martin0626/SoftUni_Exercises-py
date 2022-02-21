income = float(input())
mounths = int(input())
money_needed = float(input())

sum_save = income - (money_needed + income * 0.3)

percent = (sum_save / income) * 100

print (f'She can save {percent:.2f}%\n{(sum_save * mounths):.2f}')


