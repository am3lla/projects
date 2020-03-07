#!/usr/bin/env python3

import time, datetime

epoch_seconds = time.time()
print(epoch_seconds)

t = time.ctime(epoch_seconds)
print(t)

dt = datetime.datetime.today()
print(dt)

print(f"day: {dt.day}, month: {dt.month}, year: {dt.year}")
print(f"hour: {dt.hour}, minute: {dt.minute}, second: {dt.second}")
