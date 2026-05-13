#function is a block of code to perform a specific task when it is called 
def calculatemean(a,b):
    mean=(a+b)/(a*b)
    print(mean)

a=2
b=3
calculatemean(a,b)
#pass> used to pass and continue next step
'''2 types of functions
1.built in function- len(), min(),max(),sum()...
2.user defined function - user is created to perform special task
syntax = def function_name(parameters):
pass
'''
#arguments> are 4 types 1.default arguments > even when we created the value during func creation it always takes arguments which are below 
def count(a=2,b=2):
    print(a+b)
a=10
b=10
count(a,b)
# 2.keyword argument > it takes arguments like key=value , here order doesnt matter 
def naming(fn,mn,ln):
    print("hie ",fn , mn,ln)
fn='gajapuram'
ln='sri' 
mn='bhavya'
naming(fn,mn,ln)
#3.required argument > when we pass paramters in function then equal num of parameters= equal arguments 


