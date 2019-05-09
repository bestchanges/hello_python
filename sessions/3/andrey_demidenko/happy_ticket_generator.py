def gen_happy_ticket():
    """ The lowest happy ticket is 001001 in case of six digit number, so there is no need to start from zero """
    current_ticket_number = 1000
    while True:
        current_ticket_number += 1
        ticket = f'{current_ticket_number:06}'
        digits = [int(x) for x in ticket]
        if sum(digits[0:3]) != sum(digits[3:]):
            continue

        yield ticket


if __name__ == '__main__':
    happy_ticket_iterator = iter(gen_happy_ticket())
    while True:
        user_input = input('Press ENTER to generate happy ticket or any letter to abort...')
        if user_input == '':
            print(next(happy_ticket_iterator))
            continue

        print('Generator is aborted.')
        break
