def happy_tickets(start_from = 0):
    v = start_from
    while True:
        if v >= 1000000:
            return
        digits = [v % 10 ** x // 10 ** (x - 1) for x in range(6, 0, -1)]
        assert len(digits) == 6
        if sum(digits[0:3]) == sum(digits[-3:]):
            yield ''.join([str(i) for i in digits])
        v += 1

counter = 0
for ticket in happy_tickets():
    print(ticket)
    counter += 1
print(f"Found {counter}")
