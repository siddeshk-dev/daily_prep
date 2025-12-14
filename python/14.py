numbers = [12, 45, 7, 23, 89, 34, 56, 10, 3, 77]

print("Numbers:", numbers)

# Sum of all numbers
total = 0
for n in numbers:
    total += n
print("Total Sum:", total)

# Average
average = total / len(numbers)
print("Average:", average)

# Find largest number
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print("Largest Number:", largest)

# Find smallest number
smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n
print("Smallest Number:", smallest)

# Count even and odd numbers
even_count = 0
odd_count = 0

for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Numbers Count:", even_count)
print("Odd Numbers Count:", odd_count)

# Sum of even numbers
even_sum = 0
for n in numbers:
    if n % 2 == 0:
        even_sum += n
print("Sum of Even Numbers:", even_sum)

# Sum of odd numbers
odd_sum = 0
for n in numbers:
    if n % 2 != 0:
        odd_sum += n
print("Sum of Odd Numbers:", odd_sum)

print("Program completed successfully.")
