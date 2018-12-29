#practicepython.org - Odd or Even  

yourNum = int(input("Enter in a number: "))

if(yourNum % 2 == 0):
    print("Your number is even!")
    if(yourNum % 4 == 0):
        print("you are EVEN cooler!")
else:
    print("Your number is odd!")

'''extra 2:  Ask the user for two numbers: one number to check (call it num)
                and one number to divide by (check).
                 If check divides evenly into num, tell that to the user. If not,
                 print a different appropriate message.'''

num = int(input("Enter in a number: "))

check = int(input("Enter in another number: "))

if(num % check == 0):
    print("Both numbers you entered in are kewl numbers. ")
else:
    print("you are lame")
