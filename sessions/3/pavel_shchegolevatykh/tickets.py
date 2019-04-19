import random


def get_lucky_number():
    for num in range(100000, 999999):
        if is_lucky(num):
            yield num


def is_lucky(six_digit_number):
    sum_last_three = 0
    sum_first_three = 0
    for num_part in range(1, 4):
        sum_last_three += six_digit_number % 10
        six_digit_number //= 10
    for num_part in range(1, 4):
        sum_first_three += six_digit_number % 10
        six_digit_number //= 10
    return sum_first_three == sum_last_three


lucky_numbers = []
for lucky_number in get_lucky_number():
    lucky_numbers.append(lucky_number)

print(random.choice(lucky_numbers))
