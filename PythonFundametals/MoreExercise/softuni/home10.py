days = int(input())
type_room = input()
grade = input()
nights = days - 1
end_sum = 0


if type_room == 'room for one person':
    end_sum = nights * 18
    

elif type_room == 'apartment':
    end_sum = nights * 25
    if days < 10:
        end_sum -= end_sum * 0.3
    elif days < 15:
        end_sum -= end_sum * 0.35
    else:
        end_sum -= end_sum * 0.5

elif type_room == 'president apartment':
    end_sum = nights * 35
    if days < 10:
        end_sum -= end_sum * 0.1
    elif days < 15:
        end_sum -= end_sum * 0.15
    else:
        end_sum -= end_sum * 0.2
if grade == 'positive':
    end_sum += end_sum * 0.25
elif  grade == 'negative':
    end_sum -= end_sum * 0.1

print (f'{end_sum:.2f}')



    