def fib(length):
    seq = [0, 1]

    while len(seq) < length:
        seq.append(seq[-1] + seq[-2])

    return seq


def is_number_in(num, seq):
    if num in seq:
        return f'The number - {num} is at index {seq.index(num)}'
    return f'The number {num} is not in the sequence'

