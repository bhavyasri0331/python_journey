#multithreading > Multithreading is a technique in Python where multiple threads run concurrently within a process to improve responsiveness and handle multiple tasks simultaneously.
'''downloading files,background tasks,web requests,GUI applications,concurrent operations'''
import threading
def hello():
    print("Hello from thread")
t = threading.Thread(target=hello)
t.start()
#multiple thread example
import threading
def task(name):
    print(f"{name} is running")
t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))
t1.start()
t2.start()

#join() waits until thread finishes.
import threading
import time
def task():
    print("Started")
    time.sleep(2)
    print("Completed")
t = threading.Thread(target=task)
t.start()
t.join()
print("Main thread ends")
#Daemon Thread> Runs in background.
t = threading.Thread(target=task, daemon=True)

'''Difference Between Multiprocessing and Multithreading
Multithreading	     -    Multiprocessing
Multiple threads	 -    Multiple processes
Shared memory	     -    Separate memory
Lightweight	         -    Heavyweight'''

#Multiprocessing > Multiprocessing is a Python technique that allows multiple processes to run in parallel using separate memory spaces, mainly used for CPU-intensive tasks.
'''It helps in:parallel execution,CPU-intensive tasks,faster computation
Unlike multithreading, multiprocessing uses:separate processes,separate memory'''
import multiprocessing
def task():
    print("Process running")
p = multiprocessing.Process(target=task)
p.start()
p.join()
#multiprocess example
import multiprocessing
def show(name):
    print(f"{name} is running")
p1 = multiprocessing.Process(target=show, args=("Process-1",))
p2 = multiprocessing.Process(target=show, args=("Process-2",))
p1.start()
p2.start()
p1.join()
p2.join()