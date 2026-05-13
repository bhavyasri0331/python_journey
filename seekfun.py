'''In Python file handling, Python keeps a file pointer that shows the current position inside the file.

Functions like tell() and seek() help control that pointer.'''
#seek() moves the file pointer to a specific position.
file = open("myfile.txt", "r")
print(file.read(5))
file.seek(0)
print(file.read(5))
file.close()
#with diff position
file = open("myfile.txt", "r")
file.seek(6)
print(file.read())
file.close()
#tell() returns the current position of the file pointer.
file = open("myfile.txt", "r")
print(file.tell())
file.close()
#after reading the data
file = open("myfile.txt", "r")
print(file.read(5))
print(file.tell())
file.close()

#lambda > is a keyword used in for small ananamous function without a name to optimize the code. the keyword lambda follows syntax
#syntax: lambda arguments: expression
double = lambda x: x*2
cube = lambda y: y*y*y
avg = lambda a,b,c: a+b+c / 3
print(double(2))
print(cube(3))
print(avg(2,3,4))
#map > using in python with list
def cube(x):
    return x*x*x
print(cube(2))
l=[1,2,3,4,5]
print(list(map(cube,l)))
# filter
def filter_fun(x):
    return x>2
l2=list(filter(filter_fun,l))
print(l2)
#reduce
from functools import reduce
num=[1,2,3,4,5]
def add(x,y):
    return x+y
sum = reduce(add,num)
print(sum)
#difference btw is and ==
a=[1,2,3]
b=[1,2,3]
print(a is b) #check the exact location in the memory
print(a == b) #checks the value 
