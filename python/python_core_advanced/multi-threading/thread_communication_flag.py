#!/usr/bin/env python3

from threading import Thread
from time import sleep

class Producer:
    
    def __init__(self):
        self.products = []
        self.orders_placed = False
    
    def produce(self):
        for i in range (1, 5):
            self.products.append(f"Product {i}")
            sleep(1)
            print(f"Product {i} added")
        self.orders_placed = True

class Consumer:

    def __init__(self, producer):
        self.producer = producer
    
    def consume(self):
        
        while not self.producer.orders_placed:
            sleep(.2)
        
        print(f"Orders shipped {self.producer.products}")

p = Producer()
c = Consumer(p)

t1 = Thread(target = p.produce)
t2 = Thread(target = c.consume)

t1.start()
t2.start()
