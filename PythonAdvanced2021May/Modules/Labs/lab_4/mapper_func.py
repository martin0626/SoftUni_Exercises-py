def divide(x, y):
    print(f'{x / y:.2f}')


def multiply(x, y):
    print(f'{x * y}:.2f')


def subtract(x, y):
    print(x - y)


def add(x, y):
    print(x + y)


def raise_num(x, y):
    print(f'{x ** y:.2f}')


mapper = {'+': add, '-': subtract, '*': multiply, '/': divide, '^': raise_num}