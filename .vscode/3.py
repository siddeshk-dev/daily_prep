nums = list(map(int, input("Enter numbers: ").split()))
freq = {}

for n in nums:
    freq[n] = freq.get(n, 0) + 1

print(freq)
email = input("Enter email: ")

if "@" in email and "." in email and email.index("@") < email.index("."):
    print("Valid Email")
else:
    print("Invalid Email")
with open("log.txt", "r") as f:
    lines = f.readlines()

errors = 0
for line in lines:
    if "ERROR" in line:
        errors += 1

print("Total Errors:", errors)
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

while True:
    print("1.Add 2.Sub 3.Mul 4.Div 5.Exit")
    ch = input("Choice: ")

    if ch == "5":
        break

    a = int(input("A: "))
    b = int(input("B: "))

    if ch == "1":
        print(add(a, b))
    elif ch == "2":
        print(sub(a, b))
    elif ch == "3":
        print(mul(a, b))
    elif ch == "4":
        print(div(a, b))
