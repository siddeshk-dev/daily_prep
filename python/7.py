import time
import random
messages = [
    " Working...",
    "Still running...",
    "Processing...",
    "Keeping the program alive...",
    "Running smoothly..."
]
while True:
    print(random.choice(messages))
    time.sleep(2)
word = "APPLE"
chars = list(word)
print(chars)
for i in range(5):
    if i % 2 == 0:
        pass

