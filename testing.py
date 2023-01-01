import layla
import time

start = time.time()
for i in range(100000):
    eval(str(i) + "+2")
print(time.time() - start) #~.90 seconds

start=time.time()
for i in range(100000):
    layla.math(str(i) + "+2")
print(time.time() - start) #~.15 seconds
