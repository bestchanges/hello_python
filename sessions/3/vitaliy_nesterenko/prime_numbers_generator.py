#!/usr/bin/python
import time
import math

# Variables
prime_sequense = (2,3,5,7)
start_value = 2
result_number = 100000
result = []


# function which checks if input number is a prime number
def __if_prime(num):

    # check if even num
    if num % 2 == 0:
        # print("%s is even" % num)
        return result

    # check if num in prime_sequence
    if num in prime_sequense:
        # print("%s is Prime\n" % num)
        result.append(num)
        return result

    # initial i value
    i = 3

    # check odd num
    for i in range(i, int(math.sqrt(num))+1):
        # print("Function iteration: ", i)

        # check if odd number % == 0
        if num % i == 0:
            # print("%s Not Prime\n" % num)
            return result
        # skip odd values
        i += 2

    # print("%s is Prime\n" % num)
    result.append(num)
    return result

# MAIN


start = time.time()
while len(result) < result_number:
    # print("%s : sqrt %s" % (start_value, math.sqrt(start_value)))
    __if_prime(start_value)
    start_value += 1
    # print("Result length %s\n" % len(result))
end = time.time()

print("Result is %s, \nnumber of elements is %s \nFunction execution time: %s" % (result, len(result), end - start))