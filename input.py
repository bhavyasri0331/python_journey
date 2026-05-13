#by using input() function user takes the input
a=input("enter your name :")
print("your name is : ", a)
#by using numbers 
b = input("enter number1:")
c= input("enter number2:")
print("your first number is",b)
print("your second number is",c)
print(int(b)+int(c))

#strings > there is no effect whether we use ' or " "
first_name ="bhavya"
last_name = "sri"
print(first_name)
print(first_name[1])
d='''good morning everyone
this is bhavya
i am student from malla reddy clg
thank you'''
print(d)
#string slicing
w="gajapuram"
print(w[:4])
print(w[-2:-5])
#by using len() we can get length of the string 
print(len(w))

#conditional statements
a=int(input("enter your number:"))
if(a<18):
    print("your are not eligible to drive")
else:
    print("you can drive")

#elif 
if(a<0):
    print("number is negitive")
elif(a>1):
    if(a>=1 and a<=30):
        print("person is young")
    elif(a<=30 and a>=50):
        print("person is elder")
    else:
        print("person is older")
else:
    print("number is equal to zero")
