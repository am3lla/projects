#!/usr/bin/env python3

import logging

logging.basicConfig(filename="my_log.log", level=logging.DEBUG)
logging.critical("critical")
logging.error("error")
logging.warning("warn")
logging.info("info")
logging.debug("debug")
