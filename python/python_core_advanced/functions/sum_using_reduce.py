#!/usr/bin/env python3

from functools import reduce

lst = [5, 10, 15, 20]

reduce_lambda = lambda x, y : x + y
reduce_result = reduce(reduce_lambda, lst)
print(f"{reduce_result}")
