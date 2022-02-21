tickets = input()
tickets = [x.strip() for x in tickets.split(',')]
wining_chars = ['$', '^', '@', '#']

def is_jackpot (ticket, left_side, right_side):
    

    for wining_char in wining_chars:
        if 10 * wining_char == left_side and 10 * wining_char == right_side:
            print (f'ticket "{ticket}" - 10{wining_char} Jackpot!')
            return True
    return False

def is_win(ticket, left_side, right_side):
    
    for wining_char in wining_chars:
        if wining_char * 6 in left_side and wining_char * 6 in right_side:
            left_count = left_side.count(wining_char)
            right_count = right_side.count(wining_char)
            max_count = min(left_count, right_count)
            print (f'ticket "{ticket}" - {max_count}{wining_char}')
            return True
    return False
            



for ticket in tickets:
    left_side = ticket[0:10]
    right_side = ticket[10:20]
    
    
    if len(ticket) != 20:
        print ('invalid ticket')
        continue
    
    if is_jackpot(ticket, left_side, right_side):
        continue
    
    elif is_win(ticket, left_side, right_side):
        continue

    print (f'ticket "{ticket}" - no match')
