#!/usr/bin/env python3

import socket

host = "localhost"
port = 4000
buffer_size = 1024

s = socket.socket()
s.connect((host, port))
msg = s.recv(buffer_size)

while msg:
    print(f"Received {msg.decode()}")
    msg = s.recv(buffer_size)

s.close()
