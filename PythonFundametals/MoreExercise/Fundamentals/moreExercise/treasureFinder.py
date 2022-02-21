def treasure_found(text):
    treasure_find = ''
    for index in range(len(text)):
        if text[index - 1] == '&':
            while text[index] != '&':
                treasure_find += text[index]
                index += 1
            return treasure_find
def coordinates_found(text):
    coordinate = ''
    for index in range(len(text)):
        if text[index] == '<':
            while text[index] != '>':
                if text[index] != '<':
                    coordinate += text[index]
                index += 1
            return coordinate



key = [int(x) for x in input().split()]

message = input()

while message != 'find':
    decrypted_msg = ''
    index = 0
    for digit in message:
        
        if index < (len(key) - 1):
            decrypted_msg += chr(ord(digit) - key[index])
            index += 1
        else:
            decrypted_msg += chr(ord(digit) - key[index])
            index = 0
    
    treasure = treasure_found(decrypted_msg)
    coordinates = coordinates_found(decrypted_msg)
    print (f'Found {treasure} at {coordinates}')
    message = input()
    


