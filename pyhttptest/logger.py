import logging


formatter = logging.Formatter('%(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger = logging.getLogger('pyhttptest')
logger.addHandler(stream_handler)
