__author__ = 'ameadows'
#Based on custom logger found in etlUnit.
import logging

#Logging level for Testing.
TESTING = 21

#Logging level for Tracing.
TRACE = 5

logging.addLevelName(TRACE, 'TRACE')

def traceWrite(self, message, *args, **kws):

    self.log(TRACE, message, *args, **kws)
    logging.Logger.trace = trace

def testingWrite(self, message, *args, **kws):

    self.log(TESTING, message, *args, **kws)
    logging.Logger.testing = testing