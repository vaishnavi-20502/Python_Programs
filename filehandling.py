#"r" - read - default value. opens a file for reading, error  if the file doesn't exist
#"a" - append - opens a file for appending, creates the file if it does not exist
#"w" - write - opens a file for writing, creates the file if it does not exist
#"x" - create - creates the specified file, returns an error if the file exists
#"t" - text - default value. text mode
#"b" - binary - binary mode (e.g. images)
'''
#1
f = open("demofile.txt")
#is same as
#2
f = open("demofile.txt","rt")
#3
#same folder or same directory
f = open("demofile.txt")
print(f.read())
#4
f = open("C:\\Users\\DELL\\Documents\\demofile2.txt")
print(f.read())
#5
f = open("demofile.txt","r")
print(f.read(5))
#6
f = open("demofile.txt","r")
print(f.readline())
#7
f = open("demofile.txt","r")
print(f.read(5))
print(f.readline())
print(f.read())
#8
f = open("demofile.txt","r")
for x in f:
    print(x)
#9
f = open("demofile.txt","r")
print(f.readline())
f.close()

#10
f = open("demofile.txt","a")
f.write("\nNOW THE FILE HAS MORE CONTENT!")
f.close()
#11
f = open("demofile.txt","w")
f.write("OOPS I HAVE DELETED THE CONTENT")
f.close()
#12
f = open("demofile3.txt","x")
#13
import os
os.remove("demofile3.txt")
#14
import os
if os.path.exists("C:\\Users\\DELL\\Documents\\demofile2.txt"):
    os.remove("C:\\Users\\DELL\\Documents\\demofile2.txt")
else:
    print("The file doesn't exist")
'''
#15
