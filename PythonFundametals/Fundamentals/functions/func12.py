number = int(input())
def perfect_num (num):
    sum_numbers = 0
    for x in range (1, num):
        if num % x == 0:
            sum_numbers += x
        
    if sum_numbers == number:
        print ('We have a perfect number!')
    else:
        print ("It's not so perfect.")

perfect_num(number)
