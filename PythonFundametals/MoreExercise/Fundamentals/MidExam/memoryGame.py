sequence = input().split()
turns = 0
command = input()
while command != 'end':   
    index_1, index_2 = command.split()
    index_1 = int(index_1)
    index_2 = int(index_2)
    if len(sequence) > 0:    
        turns += 1
        if index_1 == index_2 or index_1 < 0 or index_2 < 0 or index_1 >= len(sequence) or index_2 >= len(sequence):
            print ('Invalid input! Adding additional elements to the board')
            new_element = f'-{turns}a'
            sequence.insert(len(sequence)//2, new_element)
            sequence.insert(len(sequence)//2, new_element)
            command = input()
            continue
        if sequence[index_1] == sequence[index_2]:
            print (f'Congrats! You have found matching elements - {sequence[index_1]}!')
            sequence = [x for x in sequence if x != sequence[index_1]]   
        elif sequence[index_1] != sequence[index_2]:
            print ('Try again!')
    command = input()
if len(sequence) <= 0:
    print (f'You have won in {turns} turns!')
else:
    result = ' '.join(sequence)
    print (f'Sorry you lose :(\n{result}')


