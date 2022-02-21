poroda = str(input())
gender = input()
year = 0
invalid = False
if gender == "m":
    if poroda == "British Shorthair":
        year = 13
    elif poroda == "Siamese":
        year = 15
    elif poroda == "Persian":
        year = 14
    elif poroda == "Ragdoll":
        year = 16
    elif poroda == "American Shorthair":
        year = 12
    elif poroda == "Siberian":
        year = 11
    else:
        invalid = True
        print(f"{poroda} is invalid cat!")

if gender == "f":
    if poroda == "British Shorthair":
        year = 14
    elif poroda == "Siamese":
        year = 16
    elif poroda == "Persian":
        year = 15
    elif poroda == "Ragdoll":
        year = 17
    elif poroda == "American Shorthair":
        year = 13
    elif poroda == "Siberian": 
        year = 12
    else:
        invalid = True
        print(f"{poroda} is invalid cat!")
cat_months = 12 * year / 6

if invalid == False:
    print(f"{cat_months} cat months")


