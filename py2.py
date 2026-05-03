#1
x = 1j

#display x:
print(x)

#display the data types of x :
print(type(x))

#2
x =["apple","banana","cherry"]

#display x:
print(x)

#display the data types of x :
print(type(x))

#3
x =("apple","banana","cherry")

#display x:
print(x)

#display the data types of x :
print(type(x))

#4
x ={"apple","banana","cherry"}

#display x:
print(x)

#display the data types of x :
print(type(x))

#5
x ={"name":"john","age":36}

#display x:
print(x)

#display the data types of x :
print(type(x))

#6
#frozenset freezes the values in set and makes it immutable
#It is not assured that the order of the elements will be retained
x = frozenset({"apple","banana","cherry"})

#display x:
print(x)

#display the data types of x :
print(type(x))

#7
x = True

#display x:
print(x)

#display the data types of x :
print(type(x))

#8
x = bytearray(5)

#display x:
print(x)

#display the data types of x :
print(type(x))

#9
#The b keyword instructs the python interpreter to read the string content as a sequence of bytes rather than characters
#The byte literals are used for representing binary data like images,audio,encoded texts,etc
x = b"Hello"

#display x:
print(x)

#display the data types of x :
print(type(x))

#10
x = None

#display x:
print(x)

#display the data types of x :
print(type(x))

#11
x = range(6)

#display x:
print(x)

#display the data types of x :
print(type(x))

#12
text_string = "UPES"
print("Original String:", text_string)
print("Type of String:", type(text_string))

#13
text_string = b"UPES"
print("Original String:", text_string)
print("Type of String:", type(text_string))

#14
#bytearray() method returns a bytearray object (i.e. array of bytes) which is mutable (can be modified) and returns a sequence of integrs in the range 0 <= x < 256 
prime_numbers = 3
byte_array = bytearray(prime_numbers)
print(byte_array)

#15
#not in syllabus
#utf - unicode transformation format
#utf-8 is an encoding format
str = "Welcome to UPES"

arr = bytes(str, 'utf-8')

print(arr)

#16
#Strings are converted into bytes using encoding
#The different encoding formats to which the string can be converted into bytes are ASCII,utf-8,etc

#17
var = 'Hey I am a String'.encode('ASCII')
print(var)

#18
#There is no max limit of integer in python3 and above
x = 1
y = 356567839263
z = -32564

print(type(x))
print(type(y))
print(type(z))

#19
x = 1.5
y = 356567839263.34566
z = -32564.45674

print(type(x))
print(type(y))
print(type(z))

#20
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#21
#random usually works on integers
#10 will be excluded
import random

print(random.randrange(1,10))