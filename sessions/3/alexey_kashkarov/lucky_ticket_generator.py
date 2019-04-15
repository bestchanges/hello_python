import random as rnd

LUCKY_NUM_LENGTH = 6
digits = []
for i in range(int(LUCKY_NUM_LENGTH / 2)):
    digits.append(rnd.randint(0, 9))
l_sum = sum(digits)
for i in range(int(LUCKY_NUM_LENGTH / 2) - 1):
    lo = max(0, 9 - ((int(LUCKY_NUM_LENGTH / 2) - i) * 9 - l_sum))
    hi = min(9, l_sum)
    d = rnd.randint(lo, hi)
    digits.append(d)
    l_sum -= d
digits.append(l_sum)
print("".join(str(d) for d in digits))
