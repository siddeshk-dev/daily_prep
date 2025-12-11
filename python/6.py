questions = [
    {"q": "What is the capital of India?", "a": "Delhi"},
    {"q": "What is 5 + 7?", "a": "12"},
    {"q": "Who wrote the Ramayana?", "a": "Valmiki"},
    {"q": "What is the largest planet?", "a": "Jupiter"},
]

score = 0

print("=============================")
print("         QUIZ GAME")
print("=============================")

for i, item in enumerate(questions, start=1):
    print(f"\nQuestion {i}:")
    print(item["q"])
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


