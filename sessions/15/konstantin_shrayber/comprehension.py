months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = dict(zip(months, lengths))
print(year, type(year))

long_months = {month for month in year if year[month] > 30}
print(long_months, type(long_months))

even_months = tuple([month for month in year if (months.index(month) + 1) % 2 == 0])
print(even_months, type(even_months))

a = (month for month in year if year[month] % 2 != 0)
print(a, *a, type(a))

non_i = [month for month in year if month.find('и') == -1]
print(non_i, type(non_i))

print(min(year, key=year.get))