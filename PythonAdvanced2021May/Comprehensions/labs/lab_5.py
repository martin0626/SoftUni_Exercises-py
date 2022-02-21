def is_divider(num):
    return len([num for n in range(2, 11) if num % n == 0]) > 0


start = int(input())
end = int(input())

print([num for num in range(start, end + 1) if is_divider(num)])
