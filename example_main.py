# DEBUG, INFO, WARNING, ERROR, CRITICAL

import logging
import example_sub

if __name__ == '__main__':
    logger = logging.getLogger()  # create logger instance 
    logger.setLevel(logging.DEBUG)  # handler level cannot be lower than logger instance 

    test_formatter = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
    
    # create handler for stdout. with no formatter - then add to logger
    # level is INFO
    stream_handler = logging.StreamHandler()  
    stream_handler.setLevel(logging.INFO)
    logger.addHandler(stream_handler)

    # create handler for file saving. with format - then add to logger
    # level is ERROR
    file_handler = logging.FileHandler('log.log')  
    file_handler.setFormatter(test_formatter)  
    file_handler.setLevel(logging.ERROR)
    logger.addHandler(file_handler)

    # create handler for file saving. with format - then add to logger
    # level is DEBUG
    file_debug_handler = logging.FileHandler('log_debug.log')  
    file_debug_handler.setFormatter(test_formatter)  
    file_debug_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_debug_handler)
    
    # test
    logger.debug("a_debug")
    logger.info("a_info")
    logger.warning("a_warning")
    logger.error("a_error")
    logger.critical("a_critical")
    logger.info("--")
    
    my_int = 15
    my_float = 3.14159
    my_string = "Hello Python"
    logger.info("my_int: %d, my_float: %.2f, my_string: %s", my_int, my_float, my_string)
    logger.debug("my_int * my_int: %d, my_int / my_float: %.2f, my_string: %s", my_int * my_int, my_int / my_float, my_string)
    logger.info("--")

    # test submodule
    example_sub.logging()
