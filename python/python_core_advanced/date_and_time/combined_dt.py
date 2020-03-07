#!/usr/bin/env python3

from datetime import *

d = date(2020, 5, 5)
print(d)

t = time()
print(t)

dt = datetime.combine(d, t)
print(dt)
