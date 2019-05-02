#!/usr/bin/python

import time

last_value = 1000000   # last value - 1
happy_tickets = list() # list for happy tickets


# FUNCTIONS
# 6-digit ticket number generator
def __format_number_generator(number):
    ticket = "%06d" % number
    yield ticket


# checks if it is a happy ticket
def __happy_check(last, input_set, output_list):
    for i in input_set:
        value = next(__format_number_generator(i))
        if sum(int(i) for i in value[:3]) == sum(int(i) for i in value[3:]):
            output_list.append(value)
    return output_list


# MAIN
# create set on int numbers with generator
start = time.time()
tickets = set(ticket for ticket in range(0, last_value))
end = time.time()
print("Set creation time : %s seconds" % (end - start))


# define happy_tickets with result of function __happy_check
start = time.time()
happy_tickets = __happy_check(last_value, tickets, happy_tickets)
end = time.time()
print("Happy tickets found in : %s seconds" % (end - start))

# print results
print("The number of happy tickets is %s" % len(happy_tickets))