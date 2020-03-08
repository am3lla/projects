#!/usr/bin/env python3

from threading import current_thread, Thread

def even_number(n):
    return not odd_number(n)

def odd_number(n):
    return bool(1 & n)

def identity_number(n):
    return n == n

def serie(start, end, function):
    print(current_thread().getName())
    i = start
    while i < end:
        if function(i):
            print(f"{i}", end = ' ')
        i += 1
    print()

t1 = Thread(target = serie, args = (0, 100, even_number))
t2 = Thread(target = serie, args = (0, 100, odd_number ))

t1.start()
t2.start()

serie(0, 100, identity_number)
