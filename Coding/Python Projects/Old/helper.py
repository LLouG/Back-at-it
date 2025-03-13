import logging
logger = logging.getLogger(__name__)
logger.propagate = False #remove this line to use the custom logger
logger.info('Hello from helper')