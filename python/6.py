questions = [
    {"t": "What is the capital of India?", "a": "Delhi"},
    {"t": "What is 5 + 7?", "a": "12"},
    {"t": "Who wrote the Ramayana?", "a": "Valmiki"},
    {"t": "What is the largest planet?", "a": "Jupiter"},
]
score = 0
print("=============================")
print("         QUIZ GAME")
print("=============================")

for i, item in enumerate(questions, start=1):
    print(f"\nQuestion {i}:")
    print(item["t"])
    ans = input("Your answer: ")

    if ans.strip().lower() == item["a"].lower():
        print("Correct!")
        score += 1
    else:
        
        print("Wrong! Correct answer:", item["a"])
print("\n=============================")
print("         RESULT")
print("=============================")
print("Your Score:", score, "/", len(questions))
print("Good job!" if score >= 3 else "Try again!")
nums = [1, 2, 2, 3, 3, 4]
unique = list(set(nums))
print(unique)
a = 5000
b = 100
c = a * b
print("Product =", c)
text = "hello"

