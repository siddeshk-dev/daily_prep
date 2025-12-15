numbers = [12, 45, 7, 23, 89, 34, 56, 10, 3, 77]
print("Given Numbers:", numbers)
total = 0
even_sum = 0
odd_sum = 0
even_count = 0
odd_count = 0
largest = numbers[0]
smallest = numbers[0]
for n in numbers:
    total += n
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
    if n % 2 == 0:
        even_count += 1
        even_sum += n
    else:
        odd_count += 1
        odd_sum += n
average = total / len(numbers)
print("Total Sum:", total)
print("Average:", average)
print("Largest Number:", largest)
print("Smallest Number:", smallest)
print("Even Count:", even_count)
print("Odd Count:", odd_count)
print("Even Sum:", even_sum)
print("Odd Sum:", odd_sum)
print("Program completed successfully.")

# Student Grade Calculator

name = input("Enter student name: ")
marks = int(input("Enter marks (0-100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "Fail"

print("\n----- Result -----")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)

