password = input()

def correct(pass_check):
    counter_digits = 0
    chars = 0
    valid = False
    others = False
    
    for x in pass_check:
        others_check =  not (65 <= ord(x) <= 90 or 97 <= ord(x) <= 122 or 48 <= ord(x) <= 57)
        chars += 1
        if 48 <= ord(x) <= 57:
            counter_digits += 1
        if  others_check:
            others = True
        
    first_approve = True
    if not (6 <= chars <= 10):
        print ('Password must be between 6 and 10 characters')
        first_approve = False
    if others:
        print ('Password must consist only of letters and digits')
        first_approve = False
    if counter_digits < 2:
        print ('Password must have at least 2 digits')
        first_approve = False
    if first_approve:
        print ('Password is valid')
correct(password)
        