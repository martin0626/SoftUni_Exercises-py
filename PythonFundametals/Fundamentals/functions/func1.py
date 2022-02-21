grade = float(input())

def type_grade (x):
    result = None
    if 2 <= x <= 2.99:
        result = 'Fail'
    elif 3 <= x <= 3.49:
        result = 'Poor'
    elif 3.5 <= x <= 4.49:
        result = 'Good'
    elif 4.5 <= x <= 5.49:
        result = 'Very Good'
    elif 5.5 <= x <= 6:
        result = 'Excellent'

    return result

print (type_grade(grade))
