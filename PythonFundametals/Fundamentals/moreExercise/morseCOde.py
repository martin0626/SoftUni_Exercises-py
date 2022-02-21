morse_code = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..'} 

message = input().split()
encrypted = ''
for digit in message: 
    for letter in morse_code.keys():
        if digit == '|':
            encrypted += ' '
            break
        if morse_code[letter] == digit:
            encrypted += letter
            break
        
print (encrypted)

    