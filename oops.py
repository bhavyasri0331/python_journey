#class > class is the blueprint of object
#object > object is the instance of class
#self parameter is the reference to the current instance of class , and used to access the variables in the class 
class employee(): # employee is class
    name='bhavya'
    salary=1000
    age=20
    def info(self):
        print(f"{self.name} salary is {self.salary}") 
e=employee() # e is the object if we want change class details we can remodify
e1=employee()
e2=employee()
e.name='sri'
e.salary=1200
e1.name='bhavyasri'
e1.salary=1400
e2.name='gajapuram'
e2.salary=20000
e.info()
e1.info()
e2.info()

# constructor is class used to create and intialize the objects , two types 1.default> only accept self 2.parameterized> accepts additional arguments
class person():
    def __init__(self,a,b):
        self.name=a
        self.occ=b
        print('hy i am developer')
    def info(self):
        print(f"{self.name} is a {self.occ}")
n=person('bhavya','hr')
n1=person('sri','manager')
n.info()
n1.info()

# default
class Demo:
    def __init__(self):
        print("Default constructor")
#paramterized
class Demo:
    def __init__(self, x):
        self.x = x

#getter and setter
'''In Python, getters and setters are used to:

access private data safely
update values with control
implement encapsulation'''
class Student:
    def __init__(self):
        self.__name = ""
    # setter
    def set_name(self, name):
        self.__name = name
    # getter
    def get_name(self):
        return self.__name
s = Student()
s.set_name("Bhavya")
print(s.get_name())