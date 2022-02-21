stack = []
parentheses = list(input())
balanced = True
complete_brackets = ["{}", "[]", "()"]

for bracket in parentheses:
    if bracket in '[{(':
        stack.append(bracket)

    elif bracket in '}])':
        try:
            brackets = stack.pop() + bracket
            if brackets in complete_brackets:
                continue
            else:
                print('NO')
                balanced = False
                break
        except IndexError:
            balanced = False
            print('NO')
            break

if balanced:
    print('YES')
