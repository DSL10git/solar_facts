import random
import time
# Welcome Message
print("Welcome to NONE")
a = input("Please press enter to start")
# Loading
res = 0
for i in range(1, 16):
    res += 1
    print(res)
time.sleep(0.5)
for i in range(16, 38):
    res += 1
    print(res)
time.sleep(0.8)
for i in range(38, 48):
    res += 1
    print(res)

d = random.randint(0, 4)
if d == 1 or 0:
    print("done")
else:
    print("An error occured, please wait, estamaited time 5 seconds")
    time.sleep(5.0)
