message = "  Hello, World!  "
print(message.strip())  # Output: "Hello, World!"
print(message.upper())  # Output: "HELLO, WORLD!"
print(message.replace("World", "Python"))  # Output: "Hello, Python!"
name = input("Enter the name:")
age = int(input("Enter the age: "))
print("Hello", name , "You are" , str(age) +"Years old")
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert input to integer
print("Hello, " + name + "! You are " + str(age) + " years old.")
a = ("Hello\\World")
print(a)  # Output: Hello\World