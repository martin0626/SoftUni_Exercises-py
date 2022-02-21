def comb(iterable, n, current_names=[]):
    if len(current_names) == n:
        print(', '.join(current_names))
        return

    for i in range(len(iterable)):
        current_names.append(iterable[i])
        comb(iterable[i+1:], n, current_names)
        current_names.pop()


text_l = [el for el in input().split(', ')]
dep = int(input())
comb(text_l, dep)
