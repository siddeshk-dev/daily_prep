# List Comprehension, File Handling, Lambda Functions, Recursion, OOP, Random Module, Math Module, Prime Number Checker,
#  Date and Time, Age Calculator, Fibonacci Sequence, Palindrome Checker, BMI Calculator, String Reversal, 
# Largest Number Finder, Vowel Counter, Match-Case Statement, GCD Calculator
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_squares = [n*n for n in numbers if n % 2 == 0]

print("Even squares:", even_squares)
note = input("Write your note: ")

with open("notes.txt", "a") as file:
    file.write(note + "\n")

print("Note saved successfully!")
add = lambda a, b: a + b
mul = lambda a, b: a * b

print("Add:", add(5, 3))
print("Multiply:", mul(4, 6))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)     
num = int(input("Enter a number to find its factorial: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        if self.species == "Dog":
            return "Woof!"
        elif self.species == "Cat":
            return "Meow!"
        else:
            return "Unknown sound"
dog = Animal("Buddy", "Dog")
cat = Animal("Whiskers", "Cat")
print(f"{dog.name} says: {dog.make_sound()}")
print(f"{cat.name} says: {cat.make_sound()}")
import random
def roll_dice():
    return random.randint(1, 6)
print("Rolling the dice...")
dice_result = roll_dice()
print("You rolled a:", dice_result)
import math
def calculate_circle_area(radius):
    return math.pi * radius * radius                    
radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
print("Prime numbers between 1 and 50:")
for num in range(1, 51):
    is_prime = True
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
import datetime
now = datetime.datetime.now()   
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Today's date:", now.strftime("%Y-%m-%d"))
print("Current time:", now.strftime("%H:%M:%S"))
print("Welcome to the Age Calculator!")
birth_year = int(input("Enter your birth year: "))
current_year = datetime.datetime.now().year
age = current_year - birth_year
print(f"You are {age} years old.")  
print("Thank you for using the Age Calculator!")
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]
terms = int(input("Enter the number of terms for Fibonacci sequence: "))
fib_sequence = fibonacci(terms)
print("Fibonacci sequence:", fib_sequence)
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")  
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
def reverse_string(s):
    return s[::-1]
string = input("Enter a string to reverse: ")
reversed_str = reverse_string(string)
print("Reversed string:", reversed_str)
def find_largest(numbers):
    return max(numbers)
num_list = [10, 24, 3, 56, 78, 1, 99]
largest_number = find_largest(num_list)
print("The largest number is:", largest_number)
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count
string = input("Enter a string to count vowels: ")
vowel_count = count_vowels(string)
print(f"The number of vowels in the string is: {vowel_count}")
choice = int(input("Enter a number (1-3): "))

match choice:
    case 1:
        print("You chose Python")
    case 2:
        print("You chose Java")
    case 3:
        print("You chose JavaScript")
    case _:
        print("Invalid choice")
def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = calculate_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd}")