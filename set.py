#It is a python data structure
#It is unordered ,unchangeable,unindexed,however we can remove and add new items in a set
#1
#A set can't have 2 items with same value.Duplicate items are not allowed
#The duplicate values are ignored
myset = {"apple","banana","cherry","cherry"}
print(myset)

#2
#True is considered 1 in python(True and 1 are duplicate values)
myset = {"apple","banana","cherry",True,1,2}
print(myset)

#3
#False is considered 0 in python(False and 0 are duplicate values)
myset = {"apple","banana","cherry",False,0,2}
print(myset)

#4
myset = {"apple","banana","cherry"}
print(myset)

#5
#len() function gives the number of distinct elements in set
myset = {"apple","banana","cherry","cherry"}
print(len(myset))

#6
#we can use set constructor for making a set
myset = set(("apple","banana","cherry"))
print(type(myset))

#7
#elements of set can be printed in different order since it is unordered and unindexed
myset = {"apple","banana","cherry"}

for x in myset:
    print(x)

#8
#add() function can add elements anywhere in the set
#we can't use append() function because it adds element in the last but sets are unindexed
myset = {"apple","banana","cherry"}
myset.add("orange")
print(myset)

#9
#adding 2 sets
myset = {"apple","banana","cherry","mango"}
thisset = {"pineapple","mango","papaya","apple"}
myset.update(thisset)
print(myset)

#10
#adding set and list
myset = {"apple","banana","cherry","mango"}
mylist = ["pineapple","papaya"]
myset.update(mylist)
print(myset)

#11
#adding set and tuple
myset = {"apple","banana","cherry","mango"}
mytuple = ("pineapple","papaya")
myset.update(mytuple)
print(myset)

#12
#adding multiple sets
thisset = {"apple","banana","cherry","mango"}
tropical = {"pineapple","mango","papaya","apple"}
tr = {"plum","mango","papaya","apple"}
op = {"guava"}
thisset.update(tropical,tr,op)
print(thisset)

#13
#output will always be a set
thisset = {"apple","banana","cherry","mango"}
tropical = ["pineapple","mango","papaya","apple"]
tr = ("plum","mango","papaya","apple")
op = {"guava"}
thisset.update(tropical,tr,op)
print(thisset)

#14
#only one argument will be removed using remove() and discard()
thisset = {"apple","banana","cherry","mango"}
thisset.remove("cherry")
print(thisset)

#15
#discard() only works on sets
thisset = {"apple","banana","cherry"}
thisset.discard("cherry")
print(thisset)

#16
thisset = {"apple","banana","cherry"}
thisset.remove("pineapple")
print(thisset)

#17
thisset = {"apple","banana","cherry"}
thisset.discard("pineapple")
print(thisset)

#18
#random value is popped out since sets are unindexed and pop() function deletes the value at last index
thisset = {"apple","banana","cherry"}
x = thisset.pop()
print(thisset)

#19
#no error(set is empty)
thisset = {"apple","banana","cherry"}
thisset.clear()
print(thisset)

#20
#error will be generated(set is deleted)
thisset = {"apple","banana","cherry"}
del thisset
print(thisset)

#21
#union()
set1 = {"a","b","c"}
set2 = {1,2,3,"a"}
set3 = set1.union(set2)
print(set3)

#22
#intersection_update()
#intersection and update is done in the same set
x = {"apple","banana","cherry","google"}
y = {"google","microsoft","apple"}
x.intersection_update(y)
print(x)

#23
#intersection()
#new set should be created
#improper output is generated if a new set is not created
x = {"apple","banana","cherry","google"}
y = {"google","microsoft","apple"}
z = x.intersection(y)
print(z)

#24
#no error
#intersection() function can be performed on multiple sets
x = {"apple","banana","cherry","google"}
y = {"google","microsoft","apple"}
a = {"plum","google"}
b = {"guava","google"}
z = x.intersection(x,y,a,b)
print(z)

#25
#error
#intersection_update() function can't be performed on multiple sets 
x = {"apple","banana","cherry","google"}
y = {"google","microsoft","apple"}
a = {"plum","google"}
b = {"guava","google"}
x.intersection_update(x,y,a,b)
print(z)

#26
#symmetric_difference()
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
z = x.symmetric_difference(y)
print(z)

#27
#symmetric_difference_update()
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
x.symmetric_difference_update(y)
print(x)

#28
#error
#symmetric_difference_update() function can't be performed on multiple sets 
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
a = {"plum"}
x.symmetric_difference_update(y,a)
print(x)

#29
#error
#symmetric_difference() function can't be performed on multiple sets
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
a = {"plum"}
z = x.symmetric_difference(y,a)
print(z)

