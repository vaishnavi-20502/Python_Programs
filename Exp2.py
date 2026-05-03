#1
x = 9
y = 7

sumr = x + y
subr = x - y
multr = x * y
divr = x / y

print("Sum:",sumr)
print("Subtraction:",subr)
print("Multiplication:",multr)
print("Division:",divr)

#2
import math

radius = float(input("Enter radius: "))
area = math.pi * radius * radius
print("Area of circle:", area)

#3
x = int(input("Enter number 1 : "))
y = int(input("Enter number 2 : "))

result = (x + y) * (x + y)
print("Result:", result)

#4
import math

a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))

c = math.sqrt(a ** 2 + b ** 2)
print("Length of hypotenuse:", c)


#5
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

si = (principal * rate * time) / 100
print("Simple interest:", si)

#6
import math

a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Area of triangle:", area)

#7
seconds = int(input("Enter seconds: "))

hours = seconds / 3600
minutes = (seconds % 3600) // 60
rem_sec = seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Remaining seconds:", rem_sec)

#8
x = int(input("Enter num 1 : "))
y = int(input("Enter num 2 : "))

x = x + y
y = x - y
x = x - y

print("Swapped x:", x)
print("Swapped y:", y)

#9
n = int(input("Enter number of natural numbers: "))

sum_n = n * (n + 1) / 2
print("Sum of first", n, "natural numbers:", sum_n)

#10
for i in range(2):
    for j in range(2):
        print("i:", i, "j:", j, "AND:", i & j, "OR:", i | j, "XOR:", i ^ j)
        
#11
num = int(input("Enter a number: "))

left_shift = num << 1
right_shift = num >> 1

print("Left shift:", left_shift)
print("Right shift:", right_shift)

#12
sequence = [10, 20, 56, 78, 89]

num = int(input("Enter a number: "))

if num in sequence:
    print("Number is in sequence")
else:
    print("Number is not in sequence")

#13
string = "Hello, World!"

char = input("Enter a character: ")

if char in string:
    print("Character is in string")
else:
    print("Character is not in string")