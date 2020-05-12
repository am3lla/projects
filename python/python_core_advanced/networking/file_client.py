#!/usr/bin/env python3

import socket

host = "localhost"
port = 6767
buffer_size = 1024

s = socket.socket()
s.connect((host, port))

file_name = input("Enter file name: ")

s.send(file_name.encode())
content = s.recv(buffer_size)
print(content.decode())

s.close()
