#!/usr/bin/env python3

class Duck:
    def talk(self):
        print("Duck talking...")

class Human:
    def talk(self):
        print("Human talking...")

def callTalk(obj):
    obj.talk()

d = Duck()
h = Human()

callTalk(d)
callTalk(h)
