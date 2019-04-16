import random


def happy_tickets_generator():
    sum_dict = {}

    for num in range(1000):
        i = num
        sum = 0
        for _ in range(3):
            sum += i % 10
            i //= 10
        if sum in sum_dict.keys():
            sum_dict.get(sum).append(num)
        else:
            sum_dict.update({sum: [num]})
    while True:
        random_sum = random.choice(list(sum_dict.keys()))
        happy_ticket_num = random.choice(sum_dict.get(random_sum)) * 1000 + random.choice(sum_dict.get(random_sum))
        yield "{:06d}".format(happy_ticket_num)

happy_tickets=happy_tickets_generator()
for _ in range(10):
    print(next(happy_tickets))
