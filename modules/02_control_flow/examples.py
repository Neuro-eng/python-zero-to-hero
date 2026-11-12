import random

secret = random.randint(1, 20)
for attempt in range(1, 6):
    guess = int(input(f"Attempt {attempt}/5 - guess 1..20: "))
    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")
else:
    print(f"Out of attempts. The number was {secret}")
