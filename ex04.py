#print divisors given an input 

num = int(input("Enter in a number: "))

print("Here is a list of all the divisors of that number: ")

for i in range(1, num + 1):
    if(num % i == 0):
        print(i, end = " ")
