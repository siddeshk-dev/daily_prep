num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)
numbers = [12, 1000, 3, 22, 89, 2]
largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest number:", largest)
num = int(input("Enter a number: "))

is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is a Prime Number")
else:
    print(num, "is NOT a Prime Number")
a, b = 0, 1

for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
s = input("Enter a word: ")

if s == s[::-1]:
    print("It is a Palindrome")
else:
    print("Not a Palindrome")
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n*i)
n = int(input("Enter a number: "))

for i in range(1, 10):
    print(n, "x", i, "=", n*i)
