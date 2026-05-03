#1
mytuple = ("apple","banana","cherry")
print(mytuple)

#2
mytuple = ("apple","banana","cherry","apple","cherry")
print(mytuple)

#3
mylist = ["apple","banana","cherry","apple","cherry"]
print(mytuple)

#4
mytuple = ("apple","banana","cherry","apple","cherry")
print(len(mytuple))

#5
mytuple = ("apple",)
print(type(mytuple))

#6
mytuple = ("apple")
print(type(mytuple))

#7
tuple1 = ("abc",34,True,40.3,"male")
print(tuple1)

#8
#tuple constructor
#double round brackets

mytuple = tuple(("apple","banana","cherry","apple","cherry"))
print(mytuple)

#9
#list constructor

mylist = list(("apple","banana","cherry","apple","cherry"))
print(mytuple)

#10
thistuple = ("apple","cherry","banana")
print(thistuple[1])

#11
thistuple = ("apple","cherry","banana")
if "apple" in thistuple:
    print("yes,'apple' is in the fruits tuple")

#12
x = ("apple","cherry","banana")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#13
x = ("apple","cherry","banana")
y = list(x)
y.append("orange")
x = tuple(y)
print(x)

#14
#concatenation in tuple
x = ("apple","cherry","banana")
y = ("orange",)
x += y
print(x)

#15
x = ("apple","cherry","banana")
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)

#16
x = ("apple","cherry","banana")
del x
print(x)

#17
#mapping
fruits = ("apple","banana","cherry")
(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)

#18
#unpacking of a data collection
#unpacking a tuple means to extract values of a tuple into variables.
#the number of variables must match the number of values in the tuple,
#if not, we must use an asterisk to collect the remaining values as a list

fruits = ("apple","banana","cherry","strawberry","raspberry")
(green,yellow,*red) = fruits
print(green)
print(yellow)
print(red)

#19
#error
fruits = ("apple","banana","cherry","strawberry","raspberry")
(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)

#20
fruits = ("apple","banana","cherry","strawberry","raspberry")
(green,*yellow,red) = fruits
print(green)
print(yellow)
print(red)

#21
thistuple = ("apple","banana","cherry")
for x in thistuple:
    print(x)

#22
thistuple = ("apple","banana","cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

#23
thistuple = ("apple","banana","cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i  + 1      

#24
tuple1 = ("a","b","c")
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3)

#25
fruits = ("apple","banana","cherry")
mytuple = fruits * 2
print(mytuple)

