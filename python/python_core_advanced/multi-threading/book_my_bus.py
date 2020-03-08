#!/usr/bin/env python3

from threading import current_thread, Lock, Semaphore, Thread

class BookMyBus:

    def __init__(self, available_seats):
        self.available_seats = available_seats
        #self.lock = Lock()
        self.lock = Semaphore()
    
    def buy(self, seats_requested):
        self.lock.acquire()
        print(f"Seats available: {self.available_seats}")
        if self.available_seats >= seats_requested:
            print("Confirming seat")
            print("Processing payment")
            print("Printing ticket")
            self.available_seats -= seats_requested
        else:
            print("Sorry, no seats available ")
        self.lock.release()

bmb  = BookMyBus(10)

t1 = Thread(target = bmb.buy, args = (3,))
t2 = Thread(target = bmb.buy, args = (4,))
t3 = Thread(target = bmb.buy, args = (4,))

t1.start()
t2.start()
t3.start()
