#!/usr/bin/env python3

from datetime import date
from time import sleep, perf_counter

start_seconds = perf_counter()

lst = [
    date(2016, 8, 12),
    date(2016, 7, 12),
    date(2018, 8, 12),
]

lst.sort()

sleep(3)

print(lst)
 
end_seconds = perf_counter()

print(f"Execution took: {end_seconds-start_seconds}")
