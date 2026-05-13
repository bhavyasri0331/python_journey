#list> list is a collection of ordered items where we can store the data types ,which can be alter after the creation used by [] and separated with commmas
#negative index> starts from end to begin last one -1 and last to 2nd -2
l=[1,2,3,'bhavya',True]
print(l)
print(type(l))
print(l[0])
print(l[2])
print(l[3])
print(l[4])
print(l[-3]) #prints 3
if 2 in l:
    print("yes")
else:
    print("no")
#same applies for string too 
if "bhav" in l:
    print("yes")
else:
    print("no")
#index slicing
print(l[:])
print(l[1:])
print(l[1:4:2])
#methods
l2=[1,2,3,4,5,6,3,2,8]
l2.append(9)
l2.sort()
print(l2.count(3))
l2.reverse()
print(l+l2)
m=[100,200,300]
l2.extend(m)
l2.insert(2,500)

#tuples> used to store the data items of ordered we cant alter (change) once tuple is created ()
tup=(1,2,3,4,5)
print(type(tup))
print(tup[:]) #same as list
#methods also same as list but we need to change them into tuples to list as tuples are immutable
num=(6,7,8,9)
temp=list(num)
temp.count(6)
temp.append(10)
