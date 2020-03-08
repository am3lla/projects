#!/usr/bin/env python3

from threading import current_thread, Thread
from time import sleep

class MyThread:
    def display(self):
        print(current_thread().getName())
        sleep(1)
        i = 0
        while i < 11:
            print(f"{i}", end = ' ')
            i += 1
        print()
    
    @staticmethod
    def greeting():
        print("Hello")

my_thread = MyThread()
t = Thread(target = my_thread.display)
t.start()

w = Thread(target = MyThread.greeting)
w.start()

my_thread_2 = MyThread()
t = Thread(target = my_thread_2.display)
t.start()

my_thread_3 = MyThread()
t = Thread(target = my_thread_2.display)
t.start()
