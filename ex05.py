#05 - List Overlap 
#return a list that is common with no duplicates from two arrays of different sizes.

#extra 1: randomly generate two list to test this: 

istOne = [random.choice(range(20)) for i in range(10)]
listTwo = [random.choice(range(20)) for i in range(12)]

print('List One: ', listOne)
print('List Two: ', listTwo)
print('No duplicates: ', list(set(listOne) | set(listTwo)))

#extra 2: do it with one line of code   ?????
