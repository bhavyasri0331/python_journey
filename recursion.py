#function calling itself is know ans recursion
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#fibbonaci series
def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
print(fib(6))
    
    
#sets> are unordered collection where once it is created we cant modify and duplicates are not allowed in set
s={2,3,4,5}
print(s)
#allows all datatypes to store 
b={True,2,'sri',3,2}
print(b)
#operations> update, difference , union, add,discard/remove,pop,del(delete)-it is a keyword which deletes the entire set not method,empty()
s1={1,2,3}
s2={3,4,5}
s3=s1.union(s2)
s4=s1.update(s2)
s5=s1.difference(s2)
print(s3)
print(s4)
print(s5)

#dictionarys > dict are key value pairs ,where it store the one var of many data at once and ordered collection of data 
var={ '2':'b','3':'h','4':'a','5':'v'
}
print(var.keys())
print(var.values())
print(var.items())
#dictionary methods are update,clear,pop,delete
var.update({'5':'sri'})
#we can use else block in for loop and it is gonna execute and if also can execute
for i in range(5):
    print(i)

else:
    print("there is no i")