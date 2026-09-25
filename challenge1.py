import time
start=time.time()
import random 
liste = []
for i in range(0,1000000):
    liste.insert(i,random.randint(1,10))
liste.sort(reverse=False)
print(liste)
print(time.time()-start)