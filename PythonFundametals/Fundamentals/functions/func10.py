numbers = input().split(', ')

def palidroms (nums):
    for x in nums:
        if x[0] == x[-1]:
            print ('True')
        else:
            print ('False')
palidroms(numbers)