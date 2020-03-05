#!/usr/bin/env python3

lst = [10, 2, 33, 45, 89, 2]

even_lambda = lambda n : not bool(1 & n)
odd_lambda = lambda n : bool(1 & n)

odd_numbers = list( filter(odd_lambda, lst) )
print(f"Odd numbers from list: {odd_numbers}")

even_numbers = list( filter(even_lambda, lst) )
print(f"Even numbers from list: {even_numbers}")
