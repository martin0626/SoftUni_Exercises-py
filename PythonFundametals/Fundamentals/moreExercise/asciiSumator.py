first_sumbol = input()
second_sumbol = input()
text = input()
range_sumbols = range (ord(first_sumbol)+1, ord(second_sumbol))

ascii_numbers = [ord(x) for x in text if ord(x) in range_sumbols]

print (sum(ascii_numbers))