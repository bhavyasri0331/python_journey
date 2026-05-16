#method overriding is a type of inheritance where child class redefined a method of parent class with the same name to provide specific implementation.
class parent:
    def sum(self):
        print("parent class")
class child(parent):
    def sum(self):
        print("child class")
a=child()
a.sum()

#operator overloading
class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"{self.x}i + {self.y}j "
    def __add__(self,other):
        return f"{self.x + other.x}i + {self.y + other.y}j"
v1=vector(2,3)
print(v1)
v2=vector(4,5)
print(v2)
v3=vector(6,7)
print(v1+v2)

#single inheritance > where child class inherit methods and properities from one parent class
class vehicle:
    def start(self):
        print("vehicle started")

class car(vehicle):
    def drive(self):
        print("driving done")
    
c= car()
c.start()
c.drive()

#mutiple inheritance > the class inherit methods and properities from multiple classes .
class employee:
    def __init__(self,name):
        self.name=name
class dancer:
    def __init__(self,dance):
        self.dance=dance
class employeedance(employee,dancer):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name
o=employeedance("kathak","bhavya")
print(o.name)
print(o.dance)

#multilevel inheritance > one class is inherited from another class and that class inherit from another class and it forms chain.
class a:
    pass
class b(a):
    pass
class c(b):
    pass
#example 
class grandparent:
    def house(self):
        print("grandsparent house")
class parent(grandparent):
    def car(self):
        print("parents car")
class child(parent):
    def toys(self):
        print('childrens toys')
c=child()
c.house()
c.car()
c.toys()

#hybrid inheritance > combination of one or two inheritance is called hybrid inheritance
class base:
    pass
class derived1(base):
    pass
class derived2(base):
    pass
class derived3(derived1,derived2):
    pass 
# the above syntax is combination of single and multiple inheritance

#hierarichal inheritance > multiple class inherit from same class 
class aa:
    pass
class bb(aa):
    pass
class cc(aa):
    pass
#example 
class Parent:
    def show(self):
        print("Parent method")
class Child1(Parent):
    def display1(self):
        print("Child1 method")
class Child2(Parent):
    def display2(self):
        print("Child2 method")
c1 = Child1()
c2 = Child2()
c1.show()
c1.display1()
c2.show()
c2.display2()

#Time module > The time module in Python provides functions for working with time, delays, timestamps, and formatting date/time values.
#1.time() >Returns current time in seconds from January 1, 1970 (Unix timestamp)
import time
print(time.time())
#2.ctime() > Converts timestamp into readable date and time.
print(time.ctime())
#3.sleep() > Pauses program execution for specified seconds.
import time
print("Start")
time.sleep(3)
print("End")
#4.localtime > Returns local time as structured format.
print(time.localtime())
#5.strftime > Formats date and time.
current = time.strftime("%H:%M:%S")
print(current)
date = time.strftime("%d-%m-%Y")
print(date)
#5.perf_counter() > Used to measure program execution time.
import time
start = time.perf_counter()
for i in range(1000000):
    pass
end = time.perf_counter()
print(end - start)