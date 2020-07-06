import time
from datetime import timedelta

start = time.time()

#Nuestro codigo
time.sleep(0.5)

end = time.time()

print(end - start)

start = time.monotonic()

#Nuestro código
time.sleep(1)

end = time.monotonic()

print(timedelta(seconds = end - start))
