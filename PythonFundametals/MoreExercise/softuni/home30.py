film_name = input()
all_tickets = 0
student_ticket = 0
standart_ticket = 0
kid_ticket = 0
while film_name != 'Finish':
    free_places = int(input())
    take_places = 0
    type_place = input()
    while type_place != 'End':
        take_places += 1
        all_tickets += 1
        if type_place == 'student':
            student_ticket += 1
        elif type_place == 'standard':
            standart_ticket += 1
        else:
            kid_ticket += 1
            
        if take_places == free_places:
            percent = 100/free_places * take_places
            print (f'{film_name} - {percent:.2f}% full.')
            take_places = 0
            break
        type_place = input()
        
        if type_place == 'End':
            percent = 100/free_places * take_places
            print (f'{film_name} - {percent:.2f}% full.')
            take_places = 0
            break
    film_name = input()

print (f'Total tickets: {all_tickets}')
student_ticket = 100/all_tickets * student_ticket
standart_ticket = 100/all_tickets * standart_ticket
kid_ticket = 100/all_tickets * kid_ticket
print (f'{student_ticket:.2f}% student tickets.\n{standart_ticket:.2f}% standard tickets.\n{kid_ticket:.2f}% kids tickets.')




