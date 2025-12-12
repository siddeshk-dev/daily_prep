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

