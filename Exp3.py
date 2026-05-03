#1
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Number is divisible by 3 and 5")
else:
    print("Number is not divisible by 3 and 5")

#2
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Number is multiple of 5")
else:
    print("Number is not multiple of 5")

#3
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == num2:
    print("Numbers are equal")
elif num1 > num2:
    print("First number is greater")
else:
    print("Second number is greater")
   
#4
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print("First number is greatest")
elif num2 > num1 and num2 > num3:
    print("Second number is greatest")
else:
    print("Third number is greatest")
 
#5

#6
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Year is a leap year")
        else:
            print("Year is not a leap year")
    else:
        print("Year is a leap year")
else:
    print("Year is not a leap year")
    
#7

#8
