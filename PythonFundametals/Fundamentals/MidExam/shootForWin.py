targets = [int(x) for x in input().split()]

commands = input()
shot = []
while commands != 'End':
    index = int(commands)

    if index < len(targets) and index >= 0 and targets[index] != -1:
        targets = [x - targets[index] if x > targets[index] else targets[index] + x for x in targets]
        shot.append(index)
    commands = input()


for index in shot:
    # targets.insert(index, -1)
    targets[index] = -1
targets = [str(y) for y in targets]
targets_un = ' '.join(targets)
print (f'Shot targets: {len(shot)} -> {targets_un}')

