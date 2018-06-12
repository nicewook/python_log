import logging

# create logger with module name. all named module is child of root logger
logger = logging.getLogger(__name__)  

def logging():
    
    # test
    logger.info("sub_log")