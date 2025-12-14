list = ["apple", 3, "banana", 10, "cherry", 11, "date"]
print(list)
list[0]
print(list[0])
# 2×3 matrix
matrix = [
    [1, 9, 3],
    [4, 5, 9]
]
print(matrix[1][2])   # 2 (row 0, column 1)
name = "Siddesh k"
print(name[2:6:3])# out is
print(len(name))
name = input("Enter your name: ")
name2 = input("Enter your name: ")
message = input("Enter your message: ")
message2 = input("Enter your message: ")
print(f'{name} says "{message}"')
print(f' {name2} says "{message2}"')
x = 10
x *= 10
print(x) 
a = 5
b = 10
a, b = b, a
print(a, b)
word = "mango"

for i in range(len(word)):
    print(word[i], "is at index", i)
num = 7
print("Even" if num % 2 == 0 else "Odd")

