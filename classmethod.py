#class method > A class method is a method that operates on the class rather than objects and is defined using the @classmethod decorator with cls as the first parameter.
class employee:
    company='tcs'
    def details(self):
        print(f"{self.company} has person {self.name}")

    @classmethod
    def changecompany(cls,newcompany):
        cls.company=newcompany

e=employee()
e.name='bhavya'
e.details()
e.changecompany('infosys')
e.details()
print(employee.company)
#dir> dir() functionn is used for return a list of all attributes and methods avaliable for the functions.
a=[1,2,3]
print(a.__dir__())
print(a.__len__)
#dict > __dict__ is used for returning the dictionary representation of the an object's attribute.
class dictionary:
    def __init__(self,name,age):
        self.name=name 
        self.age= age
p=dictionary('bhavyasri','20')
print(p.__dict__)
#help> help() method is used to get the discription for attributes and methods, and document of the details for object
#print(help(dictionary))


''' super() keyword is used to access:
parent class methods
parent class constructor
from the child class.
It is mainly used in inheritance.'''

class parent:
    def ab(self):
        print("parent class")
class child(parent):
    def cd(self):
        super().ab()
        print("child class")
c= child()
c.cd()

#without super keyword
class Parent:
    def __init__(self):
        print("Parent constructor")
class Child(Parent):
    def __init__(self):
        print("Child constructor")
c = Child()
#magic or dunder methods > magic methods are special methods that start and end with double underscores:
'''__init__	Constructor
__str__	String representation
__len__	Length using len()
__add__	+ operator
__sub__	- operator
__mul__	* operator
__gt__	Greater than >
__lt__	Less than <'''
#__init__
class Student:
    def __init__(self):
        print("Constructor called")
s = Student()
#__str__
class Demo:
    def __str__(self):
        return "This is demo class"
d = Demo()
print(d)
#__len__
class Students:
    def __len__(self):
        return 5
s = Students()
print(len(s))
#__add__
class Number:
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return self.num + other.num
n1 = Number(10)
n2 = Number(20)
print(n1 + n2)
