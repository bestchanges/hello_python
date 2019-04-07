import random
import sys

wrong_hits = 0
correct_hits = 0
while True:
    picked = random.randint(1, 3)
    print("Your guess: ", end='', flush=True)
    guess = sys.stdin.readline().rstrip()
    if guess == "":
        break
    if guess == str(picked):
        correct_hits += 1
        print("CORRECT! You made a good shot!")
    else:
        wrong_hits += 1
        print(f"WRONG! It was '{picked}' not '{guess}' Try again")
correct_rate = correct_hits / (correct_hits + wrong_hits)
print(f"Your hits score {round(correct_rate * 100, 1)}%. Bye!")
