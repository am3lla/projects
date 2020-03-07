#!/usr/bin/env python3

import re

s = "Take 1 up 1-3-2019 one 23 idea, one idea 45 at a time 12-11-2020"
result = re.search(r'o\w\w', s)
print(result)

if bool(result):
    print(result.group())

result = re.findall(r'o\w\w', s)
print(result)

result = re.match(r'T\w\w\w', s)
if bool(result):
    print(result.group())

result = re.split(r'\d+', s)
print(result)

result = re.sub(r'one', 'two', s)
print(result)

result = re.findall(r'o\w+', s)
print(result)

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', s)
print(result)

result = re.search(r'^T\w', s)
if bool(result):
    print(result.group())

result = re.search(r'^T\w*', s)
if bool(result):
    print(result.group())
