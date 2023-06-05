import os
import logging
from logging.handlers import TimedRotatingFileHandler as trf

class LogManager:
    
    def create_logger(self,name) -> None:
        
        if not os.path.isdir('logs'):
            os.mkdir('logs')
        
        trf_instance = trf(filename="logs/log", when="midnight", interval=1)

        logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s',
                    datefmt='[%Y-%m-%d-H%H:%M:%S]:', level=logging.INFO,
                    handlers=[trf_instance, logging.StreamHandler()])

        return logging.getLogger(name)