month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

months_dict = {name: days for (name, days) in zip(month_names, month_days)}

print(f'Dict via zip function: {months_dict}')

more_than_30_days = {name for name, days in months_dict.items() if days > 30}

print(f'More than 30 days months: {more_than_30_days}')

odd_months = [(name, days) for idx, (name, days) in enumerate(months_dict.items(), 1) if idx % 2 == 0]

print(f'Odd months: {odd_months}')
