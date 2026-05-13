# greeting a person based on time
import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
print(hour)
if(hour>12 & hour<9):
    print("good morning")
elif(hour>5 & hour<1):
    print("good noon")
else:
    print("good evening")