import layla
import time

start = time.time()
for i in range(100000):
    eval(str(i) + "+2")
print(time.time() - start) #~.90 seconds

start=time.time()
for i in range(100000):
    layla.math(str(i) + "+2")
print(time.time() - start) #~.23 seconds

start = time.time()
for i in range(100000):
    eval(str(i) + "+ abs(" + str(i) + ")")
print(time.time() - start) #1.04 seconds

start=time.time()
for i in range(100000):
    layla.math(str(i) + "+ abs(" + str(i) + ")")
print(time.time() - start) #~.35 seconds

#start = time.time()
#for i in range(100000):
#    eval(str(i) + "+ sin(" + str(i) + ")")
#print(time.time() - start) #Doesn't support sin() evalulations 

start=time.time()
for i in range(100000):
    x = layla.math(str(i) + "+ sin(" + str(i) + ")")
print(time.time() - start) #~.25 Seconds and Supports it. 