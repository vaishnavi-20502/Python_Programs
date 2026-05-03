#1
x= str(3)
y= float(3)
z= int(3)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

#2
x= "awesome"
def myfunc():
    global x
    x= "fantastic"
    print("python is "+ x)

#3
x= "awesome"
def myfunc():
    print("python is "+ x)