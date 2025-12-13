cities = ["Bengaluru", "RAMANAGARA", "Hubballi", "Mangaluru"]
for city in cities:
     print(city)
name = "Karnataka"
for letter in name:
    print(letter)  
for i in range(1, 6):
    for k in range(1, 6):
        print(f"{i} x {k} = {i * k}")
    print()  # To print an empty line after each table
    print ("Hello World!".upper()*30)
import time
print("Program started... Press Ctrl + C to stop.")
hours = 0
minutes = 0
seconds = 0
while True:
    print(f"Time Running: {hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1)
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours = 1
fruits = ["apple", "banana", "mango"]

for index, value in enumerate(fruits):
    print(index, value)
  
