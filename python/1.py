"""
n = 1
while True:
    print(10 * n )
    n += 1
"""
"""
import time

n = 1
while True:
    print("Printing number:", n)
    n += 1
    time.sleep(1)   # waits 1 second

"""
numbers = [1, 2, 3, 4]
total = 0

for n in numbers:
    total += n

print(total)


for i in range(1, 1000000000000000):
    print("Line number:", i)
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n+1):
    fact *= i

print("Factorial of", n, "is", fact)
word = "APPLE"
for ch in word:
    print(ch)
    