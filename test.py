import os
import time

# Using the timestamp string to create a
# time object/structure
from datetime import datetime


filename = r"/Users/benalaluf/Desktop/desktop_orginizer.py"
dt = datetime.fromtimestamp(os.path.getmtime(filename)).date().strftime("%d-%m-%Y")
print(dt)
print(dt.split('-'))
print(time.perf_counter())
date = {
    '2023': ('02', '03')
}
is_date = False
for year in date.keys():
    for month in date.get(year):
        if year == '2023' and month == '01':
            is_date = True

print(is_date)