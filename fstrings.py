#strings (formatted string literals) are a simple and modern way to insert variables or expressions inside strings.
#The f is written before the quotation marks.
name = "Bhavya"
age = 21

print(f"My name is {name} and I am {age} years old.")

a = 10
b = 5

print(f"Sum = {a + b}")
print(f"Multiplication = {a * b}")

#docstrings > Docstrings are special strings used to describe:
'''what a function does
what a class does
what a module does

They help others understand your code easily.'''
def greet():
    """This function greets the user."""
    print("Hello")

print(greet.__doc__)