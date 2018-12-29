#practicepython.org - Odd or Even  

yourNum = int(input("Enter in a number: "))

if(yourNum % 2 == 0):
    print("Your number is even!")
    if(yourNum % 4 == 0):
        print("you are EVEN cooler!")
else:
    print("Your number is odd!")


