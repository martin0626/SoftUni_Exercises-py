a = int(input())
name = input()
grade_sum = 0
counter = 0
fin_sum = 0
sum_1 = 0
while name != 'Finish':
    for x in range (1, a+1):
        
        grade = float(input())
        counter += 1
        sum_1 += grade 
        sum_1 /= x
        grade_sum += grade 
        if x == a:
            print (name,':',sum_1)
            sum_1 = 0 
    name = input()

fin_sum = grade_sum / counter
print (fin_sum)

    



