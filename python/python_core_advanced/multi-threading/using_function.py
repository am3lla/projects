#!/usr/bin/env python3

from threading import current_thread, Thread

def display():
    i = 0
    print(current_thread().getName())
    while i < 11:
        print(f"{i}", end = ' ')
        i += 1

print(current_thread().getName())
t = Thread(target = display)
t.start()
