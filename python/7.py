import time
import random
messages = [
    "not Working...",
    "Still running...",
    "Processing...",
    "Keeping the program alive...",
    "Running smoothly..."
]
while True:
    print(random.choice(messages))
    time.sleep(2)
word = "cherry"
chars = list(word)
print(chars)
for i in range(5):
    if i % 2 == 0:
        pass

