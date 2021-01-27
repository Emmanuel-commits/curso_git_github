import numpy as np
from time import time 

start = time.time()
for i in range(1000):
    contador +=1
    print(contador)
end = time.time()
print(f'Ha tardado: {end - start}')