#!/usr/bin/env python3

#open the file for writing
f = open("my_file.txt", "w")
s = ""
while "#" != s:
    s = input("Enter a string, # to finish: ")
    f.write(f"{s}\n")
f.close()
