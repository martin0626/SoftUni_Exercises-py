def intersection_maker(numbers):
    nums = numbers.split(',')
    x, y = int(nums[0]), int(nums[1])
    intersection = [n for n in range(x, y + 1)]
    return set(intersection)


def intersection_find(first, second):
    intersection_one = intersection_maker(first)
    intersection_two = intersection_maker(second)
    return intersection_one.intersection(intersection_two)


n = int(input())

biggest_intersection = []

for _ in range(n):
    f_intersection, s_intersection = input().split('-')
    current_intersection = intersection_find(f_intersection, s_intersection)
    if len(current_intersection) > len(biggest_intersection):
        biggest_intersection = current_intersection

print(f'Longest intersection is [{", ".join([str(el) for el in biggest_intersection])}] with length {len(biggest_intersection)}')
