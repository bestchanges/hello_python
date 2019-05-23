from rates import Rates

if __name__ == '__main__':
    rates = Rates()
    print('Print "%currency%=%amount%" to get exchange rates\n'
          'Print "Add ABC/DEF=xxx" to add exchange rate or check existing one\n'
          'print "Save" to permanently save changes\n'
          'print "Exit" to quit an application')
    while True:
        request = input('Enter your request\n')
        if '/' in request and '=' in request:
            rates.change_rate(request.split('=')[0], float(request.split('=')[1]))
        elif '=' in request:
            rates.print_rates(request.split("=")[0], float(request.split("=")[1]))
        elif request == 'Exit':
            break
        elif request == 'Save':
            rates.save_rates()
        else:
            print('Incorrect request')
