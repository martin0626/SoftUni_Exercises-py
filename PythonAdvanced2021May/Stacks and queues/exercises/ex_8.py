from collections import deque


def moving(green, free_w, cars_queue):
    time = green + free_w
    is_crashed = False
    current_car = cars_queue.popleft()
    car_length = len(current_car)

    while True:
        if car_length <= time:
            time -= car_length
            car_length = 0

        elif car_length > time:
            index_crash = car_length - time
            is_crashed = True
            return [current_car, current_car[-index_crash]], is_crashed

        if car_length == 0 and time > free_w and cars_queue:
            current_car = cars_queue.popleft()
            car_length = len(current_car)

        else:
            return cars_queue, is_crashed


green_light_duration = int(input())
free_window_duration = int(input())
cars = deque()
cars_moved = 0
crash = False

while True:

    command = input()

    if command == 'END':
        break

    elif command == 'green':
        if cars:
            cars, crash = moving(green_light_duration, free_window_duration, cars)

        if crash:
            print(f'A crash happened!\n{cars[0]} was hit at {cars[1]}.')
            break

    else:
        cars.append(command)
        cars_moved += 1

if not crash:
    print(f'Everyone is safe.\n{cars_moved - len(cars)} total cars passed the crossroads.')
