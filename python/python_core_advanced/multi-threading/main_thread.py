#!/usr/bin/env python3

import threading

current_thread = threading.current_thread()
print(f"Current running thread: {current_thread.getName()}")

main_thread = threading.main_thread()

if main_thread == current_thread:
    print("Main thread")
else:
    print("Some other thread")
