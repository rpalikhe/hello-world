from datetime import datetime
now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day

print(current_year)
print(current_month)
print(current_day)

print('%s/%s/%s %s:%s:%s' % (current_month, current_day, current_year, now.hour, now.minute, now.second))