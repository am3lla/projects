#!/usr/bin/env python3

s = "You are awesome!"
print(s)

s1 = 
"""
Your are the
creator   of 
your destiny
"""
print(s1)

print(f"{s=}, first letter is {s[0]=}")
print(f"{s*3=}")
print(f"{len(s)=}")

print(f"{s[0:5]=}")
print(f"{s[0:]=}")
print(f"{s[:8]=}")
print(f"{s[-3:-1]=}")

print(f"{s[0:9:2]=}")
print(f"{s[16::-1]=}")
print(f"{s[::-1]=}")

s2 = "   Hello world!   "
print(f"{s2.strip()=}")
print(f"{s2.lstrip()=}")
print(f"{s2.rstrip()=}")

print(f"{s.find('awe')=}")
print(f"{s.find('awe', 0, len(s))=}")
print(f"{s.count('x')=}")
print(f"{s.count('a')=}")
print(f"{s.find('x')}")
print( f"{s.replace('awesome', 'super')=}" )
print( f"{s.upper()=} {s.lower()=} {s.title()=}" )
