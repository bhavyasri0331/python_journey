#exception handling is used for handling errrors in system which detects so program runs safe without crashing
#finally> is the part of exception handling where it is always executed
a = int(input("Enter your number: "))

print(f"Multiplication table of {a} is:")

try:
    for i in range(1, 11):
        print(f"{a} * {i} = {a * i}")

except:
    print("Error occurs")
finally:
    print("always executed")

#raising custom error
n=int(input("enter num btw 5 and 9"))
if(a<5 and a>9):
    raise ValueError("value should be between 5 and 9")
# virtual environment > is used for different projects to avoid conflits betweeen them for different projects
# creating command > python -m venv myenv
#for activation > myenv scripts activate.ps1
# next pip install libraries
# for install all libraries we use command> pip install -r requirements.txt
#for deactivate command > deactivate

#IMPORT FUNCTIONS
import numpy
result= sqrt *2
print(result)
#import from
from math import sqrt,pi
result1= pi*2
print(result1)
#import as alias
from math import sqrt,pi as sp
print(sp(2))
#import from file
from function import calculatemean as cm
cm.function()




