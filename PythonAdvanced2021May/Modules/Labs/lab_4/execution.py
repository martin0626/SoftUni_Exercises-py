from mapper_func import mapper


num_1, operator, num_2 = input().split()
num_1 = float(num_1)
num_2 = float(num_2)
mapper[operator](num_1, num_2)
