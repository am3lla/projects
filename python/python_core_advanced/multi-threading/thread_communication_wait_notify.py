#!/usr/bin/env python3

from threading import Condition, Thread
from time import sleep

class Producer:
    
    def __init__(self):
        self.products = []
        self.condition = Condition()
    
    def produce(self):
        self.condition.acquire()
        for i in range (1, 5):
            self.products.append(f"Product {i}")
            sleep(1)
            print(f"Product {i} added")
        self.condition.notify()
        self.condition.release()

class Consumer:

    def __init__(self, producer):
        self.producer = producer
    
    def consume(self):
        self.producer.condition.acquire()
        self.producer.condition.wait(timeout = 0)
        print(f"Orders shipped {self.producer.products}")
        self.producer.condition.release()

p = Producer()
c = Consumer(p)

t1 = Thread(target = p.produce)
t2 = Thread(target = c.consume)

t1.start()
t2.start()
