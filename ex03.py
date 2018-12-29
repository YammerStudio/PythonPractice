

a = [1 , 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#print out elements less than five
b = []

for num in a:
    if(num <= 5):
        b.append(num)

print(b)


#extra part b: write this in one line of code -> review list comprehesion ? 


#extra part c: get an input and print out numbers that are less than input of array

num = int(input("Enter in a number: "))
d = []

for i in a:
    if(i < num):
        d.append(i)

print(d)
