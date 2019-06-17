month_names = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
               'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


month_dict = dict(zip(month_names, month_lengths))
# second option
# month_dict = {k: v for k in month_names for v in month_lengths}
print(month_dict)

set_of_longer_30 = set(k for (k, v) in month_dict.items() if v > 30)
print(set_of_longer_30)

even_months = tuple(m for i, m in enumerate(month_names) if i % 2)
print(even_months)

odd_length_months_generator = (m for (m, l) in month_dict.items() if l % 2)
while 1:
    try:
        print(next(odd_length_months_generator))
    except StopIteration:
        break

months_without_i = [m for m in month_names if 'и' not in m]
print(months_without_i)

shortest_month = min(month_dict, key=lambda m: month_dict[m])
# second option
# shortest_month = min(month_dict, key=month_dict.get)
print(shortest_month)