#print divisors given an input 

num = int(input("Enter in a number: "))

print("Here is a list of all the divisors of that number: ")
rangee = range(1, num + 1)
a = [x for x in rangee if num % x == 0]
print(a)
