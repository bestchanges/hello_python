months = (
    'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
    'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
)
lengths = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

year = dict(zip(months, lengths))
print(year, type(year))

long_months = {month for month, length in year.items() if length > 30}
print(long_months, type(long_months))

even_months = tuple([month for month, length in year.items() if length % 2 == 0])
print(even_months, type(even_months))

a = (x for x in year if year[x] % 2 != 0)
print(a, *a, type(a))

non_i = [x for x in year if x.find('и') == -1]
print(non_i, type(non_i))

print(min(year, key=year.get))
