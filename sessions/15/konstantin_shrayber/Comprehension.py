months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = dict(zip(months, lengths))
print(year, type(year))

long_months = {x for x in year.keys() if year[x] > 30}
print(long_months, type(long_months))

even_months = tuple([x for x in year.keys() if year[x] % 2 == 0])
print(even_months, type(even_months))

a = (x for x in year.keys() if year[x] % 2 != 0)
print(a, *a, type(a))

non_i = [x for x in year.keys() if x.find('и') == -1]
print(non_i, type(non_i))

print(min(year, key=year.get))