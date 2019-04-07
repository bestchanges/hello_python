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
        print("CORRECT! You make a good shot!")
    else:
        wrong_hits += 1
        print(f"WRONG! It was '{picked}' not '{guess}' Try again")
print(f"Your hits score {round(correct_hits / (correct_hits + wrong_hits) * 100, 1)}%. Bye!")
