from datetime import datetime
from datetime import date

month, d, y, time = input().split()

d = d.rstrip(',')
h, m = time.split(':')
month = datetime.strptime(month, '%B').strftime('%m')
month, d, y, h, m = int(month), int(d), int(y), int(h), int(m)


first_day = datetime(y, 1, 1)
last_day = datetime(y+1, 1, 1)
today = datetime(y, month, d, h, m)
today_long = today - first_day
year_long = last_day - first_day

print((today_long / year_long) * 100)