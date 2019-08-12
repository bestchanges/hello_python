names = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь",
         "декабрь"]
durations = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

months = dict(zip(names, durations))

months_gt_30d = {m for m, d in months.items() if d > 30}
even_months = tuple(m for m in names if names.index(m) % 2 == 0)
odd_days_months = (m for m, d in months.items() if d % 2 != 0)
months_without_letter = [m for m in names if "и" not in m.lower()]
shortest_month = min(names, key=len)

print(months)
print(months_gt_30d)
print(even_months)
print(type(odd_days_months))
for m in odd_days_months:
    print(m)
print(months_without_letter)
print(shortest_month)
