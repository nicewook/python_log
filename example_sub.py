import logging

# create logger with module name. all named module is child of root logger
logger = logging.getLogger(__name__)  

def logging():
    
    # test
    logger.debug("a_debug")
    logger.info("a_info")
    logger.warning("a_warning")
    logger.error("a_error")
    logger.critical("a_critical")
    logger.info("--")
