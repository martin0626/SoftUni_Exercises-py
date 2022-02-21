from collections import deque


pizzas = deque([int(x) for x in input().split(', ')])
employees = [int(x) for x in input().split(', ')]
total_pizza = 0

while pizzas and employees:
    pizza = pizzas.popleft()
    employee = employees.pop()
    if pizza <= 0 or pizza > 10:
        employees.append(employee)
        continue

    if employee <= 0:
        pizzas.appendleft(pizza)
        continue

    if employee >= pizza:
        total_pizza += pizza

    elif employee < pizza:
        pizza -= employee
        total_pizza += employee
        pizzas.appendleft(pizza)

if not pizzas:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizza}')
    if employees:
        print(f'Employees: {", ".join([str(n) for n in employees])}')

else:
    print(f'Not all orders are completed.\nOrders left: {", ".join([str(n) for n in pizzas])}')



