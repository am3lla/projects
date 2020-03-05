#!/usr/bin/env python3

lst = [2, 3, 4, 5, 6]

double_lambda = lambda n : 2*n

double_lst = list( map(double_lambda, lst) )

print(f"Doubled values: {double_lst}")
