"""
custom_logging.py handles the customized logging for dataNexus.  This takes advantage of Python's built in logging
library but adds more specifics to dataNexus (log format, new levels, etc.).
"""

import logging


__author__ = 'coty, ameadows'



# The TRACE category is for things that are more fine grained than DEBUG
TRACE = 5
logging.addLevelName(TRACE, 'TRACE')


def trace(self, message, *args, **kwargs):
    """
    This method creates the trace method for the logger, allowing log.trace() to be used in code.
    :param message:
    :param args:
    :param kwargs:
    :return:
    """

    self.log(TRACE, message, *args, **kwargs)
    logging.Logger.trace = trace

TESTING = 21
logging.addLevelName(TESTING, 'TESTING')

# The TESTING category was created to test options when opt is used, so that the ouput is printed from test logging.

def testing(self, message, *args, **kwargs):
    """
    This method creates the testing method for the logger, allowing log.testing() to be used in code.  This level is for
    preview mode that the application can run to verify what is generated instead of writing it to file like normal.
    :param message:
    :param args:
    :param kwargs:
    :return:
    """

    self.log(TESTING, message, *args, **kwargs)
    logging.Logger.testing = testing