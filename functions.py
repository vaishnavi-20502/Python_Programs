'''
#A function is a block of code which only runs when it's called
#1
def my_func():
    print("Hello, World!")

my_func()

#2
#Functions can take parameters
def my_func(fname):
    print(fname + " Patel")

my_func("Abhishek")
my_func("Tina")
my_func("David")

#3
#Type error will be generated
def my_func(fname):
    print(fname + " Patel")

my_func()
my_func("Tina")
my_func("David")

#A parameter is the variable listed in the parenthesis in the function definition
#fname is a parameter
#4
def my_func(fname,lname):
    print(fname + " " + lname)

my_func("Abhishek","Joshi")

#5
def my_func(fname,lname):
    print(fname + " " + lname)

my_func("Abhishek","")

#6
#Arbitrary arguments *arg - If we don't know how many arguments that will be passed into a function,
#we add a * before the parameter name in the function definition
#The arbitrary arguments are passed into the function as a tuple and are accessed through their index
def my_func(*kids):
    print("The youngest child is " + kids[2])

my_func("Abhishek","Tina","David","Sonia","Palak")

#7
#Keyword Arguments
def my_func(child3,child2,child1):
    print("The youngest child is " + child3)

my_func(child1 = "Abhi", child2 = "Tina", child3 = "Sonia")

#8
#Arbitrary Keyword Arguments
#This way the function will receive a dictionary of arguments and can access the items accordingly
def my_func(**kid):
    print("His last name is " + kid["lname"])

my_func(fname = "Abhishek",lname = "Joshi")

#Add 10 to argument a and return the result
#try to use minimum lines of code
def this_func(a):
    return a + 10  
print(this_func(5))

#Python Lambda
#A lambda function is a small anonymous function
#Lambda functions can take any number of arguments
#1
x = lambda a : a + 10
print(x(5))

#2
x = lambda a,b : a * b
print(x(5,6))

#3
x = lambda a,b,c : a + b + c
print(x(5,6,2))

#This code represents the following:
# Suppose we have a function definition that takes one argument and that argument will be multiplied with an unknown number
#use that function definition to make a function that will always double the number that you send in
#1
def my_func(n):
    return lambda a : a * n
mydoubler = my_func(2)

print(mydoubler(11))

#2
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
'''
#Python Arrays
#Python doesn't have built in support for arrays, but python lists can be used instead

#Arrays
#This page shows us how to use LISTS as ARRAYS however to work with arrays in python we will have to import a library like the NumPy library

#Arrays are used to store multiple values in one variable