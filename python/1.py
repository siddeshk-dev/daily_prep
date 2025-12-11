import time
import random

it = [
    "Working...",
    "Still running...",
    "Processing...",
    "Keeping the program alive...",
    "Running smoothly..."
]

while True:
    print(random.choice(it))
    time.sleep(2)
num = 1

while num < 10**15:       # one quadrillion
    print(num)
    num += 1
print("Matrix:")
for row in matrix:
    print(row)