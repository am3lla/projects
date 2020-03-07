#!/usr/bin/env python3

import os, sys
import logging

file_name = "my_file.txt"

if os.path.isfile(file_name):
    try:
        
        #opens the file for reading
        f = open(file_name, "r")
        s = f.read()
        print(s)
    finally:
        f.close()
else:
    logging.error(f"File {file_name} does not exists")
    sys.exit()

