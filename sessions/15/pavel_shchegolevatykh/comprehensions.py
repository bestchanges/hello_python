month_names =\
    ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сетнябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

months_dict = {name: days for (name, days) in zip(month_names, month_days)}
print(f'Dict via zip function: {months_dict}')

more_than_30_days = {name for name, days in months_dict.items() if days > 30}
print(f'More than 30 days months: {more_than_30_days}')

odd_months = [(name, days) for idx, (name, days) in enumerate(months_dict.items(), 1) if idx % 2 == 0]
print(f'Odd months: {odd_months}')

even_months_generator = (name for name, days in months_dict.items() if days % 2 != 0)
print(f'First even days month: {next(even_months_generator)}')
print(f'Second even days month: {next(even_months_generator)}')
print(f'Third even days month: {next(even_months_generator)}')

no_i_in_names = [name for name, days in months_dict.items() if 'И' not in name]
print(f'No i in month names: {no_i_in_names}')

min_month = [name for name, days in months_dict.items() if days == min(months_dict.values())]
print(f'Min month: {min_month}')
