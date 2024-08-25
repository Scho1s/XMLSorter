"""
    Author      - Val J.
    Date        - 26/08/2024
    Updated     - 26/08/2024
    Dsecription - class for initialising a logger.
"""


import logging
from datetime import datetime

class Logger:
    def __init__(self, name, filename='activity.log', level=logging.INFO):
        self.logger = logging.getLogger(name)
        logging.basicConfig(filename=filename, level=level)

    def info(self, message):
        self.logger.info(f"{datetime.now()}: {message}")


if __name__ == '__main__':
    logger = Logger(__name__)
    logger.info('trial')        # Test