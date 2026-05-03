#1

a = "hello world!"
print(a[1])

#2
#end operator keeps the pointer in the same line
for x in "banana":
    print(x,end = "")

#3
a = "hello world!"
print(len(a))

#4
a = "djitbsi    wodvvh~!@##$%^&&*("
print(len(a))

#5
txt = "the best things in life are free!"
if "free" in txt:
    print("yes,'free' is present.")

#6
txt = "the best things in life are free!"
print("expensive" not in txt)

#7
#element at 5th index is excluded
b = "hello world!"
print(b[2:5])

#8
b = "hello world!"
print(b[2:25])

#9
b = "hello world!"
print(b[15:25])

#10
b = "hello world!"
print(b[:5])

#11
b = "hello world!"
print(b[2:])

#12
b = "hello world!"
print(b[:])

#13
#negative indexing starts from the last i.e. "!" is at -1 index
b = "hello world!"
print(b[-5:-2])

#14
b = "hello world!"
print(b[-50:-5])

#15
#3rd argument stands for step size
b = "hello world!"
print(b[2:11:2])

#16
a = "Hello World!"
print(a.upper())

#17
a = "Hello World!"
print(a.lower())

#18
#strip() function is used for removing whitespaces
#it does not remove the blank spaces in between
a = "   Hello World!   "
print(a)
print(a.strip())

#19
a = "Hello World!"
print(a.replace('H','J'))

#20
a = "Hello World!"
print(a.replace('He','Ji'))

#21
a = "Hello World!"
print(a.replace('H','Ji'))

#22
#returns a list ['Hello','World','hi!']
a = "Hello,World,hi!"
print(a.split(","))

#23
a = "Hello World,hi!"
print(a.split(" "))

#24
a = "Hello!World,hi!"
print(a.split("!"))

#25
a = "Hello World,hi!"
print(a.split("l"))

#26
txt = "hello, and welcome to my world"
x = txt.capitalize()
print(x)

#27
#The first character is converted to upper case and the rest is converted to lower case
txt = "python is FUN!"
x = txt.capitalize()
print(x)

#28
txt = "36 is my age."
x = txt.capitalize()
print(x)

#29
#casefold() makes the string lower case
txt = "Hello And Welcome To My World!"
x = txt.casefold()
print(x)

#30
#The center() method will center align the string, using a specified character (space is default) as the fill character.
txt = "banana"
x = txt.center(20)
print(x)

#31
txt = "banana"
x = txt.center(20,"O")
print(x)

#32
#The count() method returns the number of times a specified value appears in the string.
txt = "I love apples, apple is my favourite fruit"
x = txt.count("apples")
print(x)

#33
txt = "I love apples, apple is my favourite fruit"
x = txt.count("apples",10,24)
print(x)

#34
#The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
txt = "My name is Ståle"
x = txt.encode()
print(x)

#35
#xml - extensible markup language
txt = "My name is Ståle"
print(txt.encode(encoding = "ascii",errors = "backslashreplace"))
print(txt.encode(encoding = "ascii",errors = "ignore"))
print(txt.encode(encoding = "ascii",errors = "namereplace"))
print(txt.encode(encoding = "ascii",errors = "replace"))
print(txt.encode(encoding = "ascii",errors = "xmlcharrefreplace"))

#36
#The endswith() method returns True if the string ends with the specified value, otherwise False.
txt = "Hello, welcome To My World."
x = txt.endswith(".")
print(x)

#37
txt = "Hello, welcome To My World."
x = txt.endswith("My World.") 
print(x)

#38
txt = "Hello, welcome To My World."
x = txt.endswith("My World.",5,11)
print(x)

#39
#The expandtabs() method sets the tab size to the specified number of whitespaces.
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)

#40
txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs(0))
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

#41
#The find() method finds the first occurrence of the specified value.
txt = "Hello, welcome To My World."
x = txt.find("welcome")
print(x)

#42
txt = "Hello, welcome To My World."
x = txt.find("e")
print(x)

#43
txt = "Hello, welcome To My World."
x = txt.find("e",5,10)
print(x)

#44
txt = "Hello, welcome To My World."
print(txt.find("q"))
print(txt.index("q"))

#45
txt = "for only {price:.2f} dollars!"
print(txt.format(price = 49))

#46
txt1 = "My name is {fname}, I'm {age}".format(fname = "John",age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)

#47
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

#48
txt = "Hello, welcome to my world."
x = txt.index("e")
print(x)

#49
txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)

#50
txt = "Hello, welcome to my world."
print(txt.find("q"))
print(txt.index("q"))

#51
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

#52
txt = "banana"
x = txt.ljust(20, "O")
print(x)

#53
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

#54
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))

#55
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))

#56
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(txt.maketrans(x, y, z))

#57
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

#58
txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)

#59
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

#60
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(True)
print(x)