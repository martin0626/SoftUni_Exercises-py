from sys import maxsize

rows, cols = [int(n) for n in input().split()]

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

max_sum = -maxsize

nums = []


for r in range(rows - 2):
    for c in range(cols - 2):
        curr_nums = [matrix[r][c], matrix[r][c + 1], matrix[r][c + 2], matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2], matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2]]
        if max_sum < sum(curr_nums):
            max_sum = sum(curr_nums)
            nums = curr_nums


print(f'Sum = {max_sum}')
print(f'{" ".join(str(n) for n in nums[:3])}\n{" ".join(str(n) for n in nums[3:6])}\n{" ".join(str(n) for n in nums[6::])}')


# from sys import maxsize
#
# row_count, column_count = [int(x) for x in input().split()]
#
# matrix = []
# for _ in range(row_count):
#     numbers = [int(y) for y in input().split()]
#     matrix.append(numbers)
#
#
# biggest = -maxsize
# biggest_cube = []
# for row in range(row_count - 2):
#     for column in range(column_count - 2):
#         cube = [matrix[row][column], matrix[row][column + 1], matrix[row][column + 2], matrix[row + 1][column], matrix[row + 1][column + 1], matrix[row + 1][column + 2], matrix[row + 2][column], matrix[row + 2][column + 1], matrix[row + 2][column + 2]]
#         if sum(cube) > biggest:
#             biggest = sum(cube)
#             biggest_cube = [str(x) for x in cube]
# print(f'Sum = {biggest}')
# print(biggest_cube[0], biggest_cube[1], biggest_cube[2])
# print(biggest_cube[3], biggest_cube[4], biggest_cube[5])
# print(biggest_cube[6], biggest_cube[7], biggest_cube[8])



