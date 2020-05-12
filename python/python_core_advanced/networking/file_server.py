#!/usr/bin/env python3

import socket

host = 'localhost'
port = 6767
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
print(f"Server listening on port {port}")

s. listen(1)
connection, address = s.accept()

print(f"Connection from {str(address)}")

file_name = connection.recv(buffer_size)

try:
    f = open(file_name, "rb")
    content = f.read()
    connection.send(content)
    f.close()
except FileNotFoundError:
    connection.send(b"File not found")

connection.close()
