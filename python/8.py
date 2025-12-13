set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  
print("Union of set1 and set2:", union_set)
day = "Saturday"
is_raining = False
if day == "Saturday" or day == "Sunday":
    if not is_raining:
        print("Let's visit Mysuru!")
    else:
        print("It's raining, let's stay home.")
else:
    print("It's a weekday, let's wait for the weekend.")        
age = 65
if age < 5:
    print("ticket is free. ")
elif age <= 12:
    print("you get a child discount. ")
elif age >= 60:
    print("you get a senior citizen discount. ")
else:
    print("tou pay the full fare. ")\

cities = ["code is 562159", "ramanagara", "Hubballi", "Mangaluru"]
for city in cities:
     print(city)
name = "Karnataka"
for letter in name:
    print(letter) 
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print() 
     # To print an empty line after each table 
print("Daily update")
for day in range(1, 8):
    print(f"Day {day}: it's my daily routine!")
fruits = ["apple", "banana", "mango"]

if "apple" in fruits:
    print("Apple found")
