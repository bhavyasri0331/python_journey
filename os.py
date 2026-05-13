#os > operatin system The built-in Python module Python os is used to interact with the operating system.
''' It helps you:

work with files and folders
create/delete directories
get current directory
rename files
run system commands
access environment variables'''
import os
print(os.getcwd()) #getcwd() → Get Current Working Directory
print(os.listdir())
os.mkdir("NewFolder")
os.rmdir("NewFolder")
print(os.path.exists("data.txt"))

#local and global  variables
#local> it can be accessed inside the function only called local variable 
def name():
    student='bhavya'#local
    print(student)
name()

#global > can be accesed outside or anywhere in the function called global variable
student='sri' #global
def named():
    print(student)
named()
print(student)

#modified global variable
student1='gajapuram'
def surname():
    global student1
    student1='bhavya gajapuram'
surname()
print(student1)

#without global
x = 5
def test():
    x = 10
    print(x)
test()
print(x)

#file handling i/p and o/p
file= open('myfile.txt','r')
print(file)
file.close()
file= open('myfile.txt','w')
file.write('file is written')
file.close()
file = open("myfile.txt", "a")
file.write("\nNew Line Added")
file.close()
with open("myfile.txt", "r") as file:
    print(file.read())

import os
if os.path.exists("myfile.txt"):
    print("File exists")
else:
    print("File not found")

#readline()> used for reading multiple lines with using loop called readline
f=open('myfile.txt','r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)

    