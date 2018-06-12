import logging

# create logger with module name. all named module is child of root logger
logger = logging.getLogger(__name__)  

# adding handler to logger makes propagation
stream_handler = logging.StreamHandler()  
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)

# this will prevent propagation to root logger
logger.propagate = False

def logging():
    
    # test
    logger.info("sub_log")