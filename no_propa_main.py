import logging
import no_propa_sub

if __name__ == '__main__':
    logger = logging.getLogger()  # create logger instance 
    logger.setLevel(logging.DEBUG)  # handler level cannot be lower than logger instance 

    test_formatter = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
    
    # create handler for stdout. with no formatter - then add to logger
    # level is INFO
    stream_handler = logging.StreamHandler()  
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(test_formatter)
    logger.addHandler(stream_handler)

    logger.info("main_log")
    no_propa_sub.logging()