import rates


def main():
    rates.load_rates()
    rates_changed = False
    print("""Available commands:
    %amount% %currency% - convert with all available rates
    %currency1%/%currency2%=%rate% - update or add rate
    download %currency1%/%currency2% - download latest rate for currencies
    rates - print all rates
    exit - exit converter
    
    """)
    while True:
        cmd = input("input: ")
        if cmd == "exit":
            if rates_changed and input("Save rates (y/n)? ") == "y":
                rates.save_rates()
            exit(0)
        elif cmd == "rates":
            print("\n".join(f"{k} = {v}" for k, v in rates.rates.items()))
        elif "download" in cmd:
            try:
                cmd = cmd.split(" ")[1]
                cmd = cmd.split("/")
                rates.download(cmd[0].upper(), cmd[1].upper())
                rates_changed = True
            except IndexError:
                print("Invalid input.")
            except ConnectionError:
                print("Cannot download rate.")
        elif "=" in cmd and "/" in cmd:
            cmd = cmd.split("=")
            try:
                rate = float(cmd[1])
                rates.update(cmd[0][0:3].upper(), cmd[0][4:7].upper(), rate)
                rates_changed = True
            except ValueError:
                print("Invalid input.")
        else:
            cmd = cmd.split(" ")
            try:
                amount = float(cmd[0])
                currency = cmd[1].upper()
                rates.convert(amount, currency)
            except ValueError:
                print("Invalid input.")
            except AssertionError as e:
                print(e)


if __name__ == '__main__':
    main()
