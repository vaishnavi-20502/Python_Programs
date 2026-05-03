#1
'''
a = 1
n = int(input("Enter a non-negative number:"))
if n < 0:
    print("Invalid Input")
else:
    for i in range(1,n+1):
        a = a*i
    print("the factorial of number",n,"is",a)
#2
c = 0
a = int(input("Enter a number:"))
temp = a
length = len(str(a))
while temp > 0:
    b = temp%10
    c = c + b**length
    temp = temp//10
if a == c:
    print("The given number is Armstrong")
else:
    print("The given number isn't Armstrong")

#3
x = int(input("Enter the number of terms:"))
a = 0
b = 1
print(a,b,end = " ")
for i in range(1,x - 1):
    c = a + b
    a = b
    b = c
    print(c,end =" ")
    i = i + 1

#4  
a = int(input("Enter a number:"))
b = 0
for x in  range (2,a):
    if (a % x) == 0:
        b = b + 1
        print("The number is not prime")
        break
if (b == 0):
    print("The number is prime")

#5
a = int(input("Enter a number:"))
temp = a
b = 0
while temp > 0:
    c = temp % 10
    b = b * 10 + c
    temp = temp // 10
if (a == b):
    print("The number is palindrome")
else:
    print("The number isn't palindrome")

#6
a = int(input("Enter a number:"))
b = 0
while a > 0:
    c = a % 10
    b = b + c
    a = a // 10
print("The sum of digits is",b)

#7
count = 0
for x in range (1,101):
    if(x % 5 == 0 or x % 7 == 0):
        count = count + 1
        print(x)
print("numbers divisible by 5 and 7 between 1 and 100 are",count)

#8
a = input("Enter a string:")
for x in a:
    print(x.upper(),end="")
'''
#9
