def recursive_power(num, rate, result=1):
    if rate == 0:
        return result
    return recursive_power(num, rate - 1, result*num)


print(recursive_power(2, 10))
print(recursive_power(10, 100))
