#!/usr/bin/env python

start = 1
end = 20

print(f"Numbers from {start} to {end} skipping multiples of 3, for version")

for i in range(start, end + 1):
    if 0 == i % 3:
        continue
    print(i, end = ' ')


print(f"\nNumbers from {start} to {end} skipping multiples of 3, while version")

i = start - 1

while i < end + 1:
    i += 1
    if 0 == i % 3:
        continue
    print(i, end = ' ')

print()
