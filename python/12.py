numbers = [12, 89, 45, 33, 10, 78]

numbers.sort()
print("Second Largest =", numbers[-2])
num = int(input("Enter number: "))
total = 0

while num > 0:
    total += num % 10
    num //= 10

print("Sum of digits =", total)
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)
text = input("Enter text: ")
upper = lower = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n+1):
    fact *= i

print("Factorial =", fact)
