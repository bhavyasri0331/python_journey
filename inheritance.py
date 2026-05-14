#inheritance > one class is inherited from another class is called inheritance , where child cls is inherited from parent class it methods,properities,and in addition it has its own.
class employee:
    def __init__(self,name,id):
        self.name= name 
        self.id= id
    def showdetails(self):
        print(f" the employee name of {self.id} is {self.name}")
    
class student(employee): #inherited class from parent(employee class)
    def participation(self):
        print('students go to college')

e1= employee('bhavya','86')
e1.showdetails()
e2=student('sri','1')
e2.showdetails()
e2.participation()
''' there are types of inheritance single level ,multiple level,multilevel,inherited,hierarichal'''

#public access modifier > in python there is no private all the variables, methods are in python are default public, any instance variable in class followed by keyword self that has self.name are public acessed
class bhavya:
    def __init__(self):
        self.name="bhavyasri" # public variable
b1= bhavya()
print(b1.name) 

#Protected members are written using a single underscore _ , They should be accessed only inside class and child class.
class sri:
    def __init__(self):
        self._name="gajapuram" # protected variable
b2=sri()
print(b2._name)

#Private members are written using double underscore __ , They cannot be accessed directly outside the class.
class marks:
    def __init__(self):
        self.__total = 500
    def show(self):
        print(self.__total)
m = marks()
m.show()

# static method is a method that belongs to the class and does not access instance or class variables. It is defined using the @staticmethod decorator.
class greet():
    @staticmethod
    def wishes():
        print("hello")
greet.wishes()
# example 2
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
print(Calculator.add(10, 20))


#class and instance variable > A class variable is shared among all objects of a class, while an instance variable is unique to each object and is defined using self.
class Employee:
    company = "Infosys"   # class variable
    def __init__(self, name):
        self.name = name  # instance variable
e1 = Employee("Bhavya")
e2 = Employee("Sri")
print(e1.company, e1.name)
print(e2.company, e2.name)
