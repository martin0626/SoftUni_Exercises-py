n = int(input())
l = int(input())
stri = ''
for x in range (1 , n + 1):
    stri += str(x)
    
    for y in range (1, n + 1):
        stri += str(y)
        
        for z in range (97, 97 + l):
            stri += chr(z)
            
            for k in range (97, 97 + l):
                stri += chr(k)
                
                for j in range (2, n +1):
                    stri += str(j)
                    stri += ' '
                    

                    
                    
print (stri)
                    
