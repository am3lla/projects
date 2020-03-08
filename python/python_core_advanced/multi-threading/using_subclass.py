#!/usr/bin/env python3

from threading import current_thread, Thread

class MyThread(Thread):
    def run(self):
        i = 0
        print(current_thread().getName())
        while i < 11:
            print (f"{i}", end = ' ')
            i += 1

print(current_thread().getName())
t = MyThread()
t.start()
