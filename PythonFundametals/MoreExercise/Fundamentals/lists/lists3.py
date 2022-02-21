def words (word):
    count = 0

    for w in word:
        if len(w) > 1 and w[0]==w[-1]:
            count += 1
    return count 

print (words (['abc', 'aba', 'bca', '1221']))