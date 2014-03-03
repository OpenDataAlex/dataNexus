__author__ = 'ameadows'

"""
settingsManager handles building the standard directories used by dbNexus,
copies the default settings files, and building the array that stores all the parameters
from the settings files.
"""
import logging
from ConfigParser import SafeConfigParser
from shutil import copyfile
from os import makedirs, path

import appdirs


appName = 'dbNexus'
appAuthor = 'BlueFireDS'
settingsFile = 'dbNexus.properties'

userSettings = appdirs.user_data_dir(appName, appAuthor)
userLogging = appdirs.user_log_dir(appName, appAuthor)


def first_run_test():
    """
    Tests if the directories used for user settings exist or not.  No parameters are passed from outside settingsManager.
    """

    if not path.isdir(userSettings):
        logging.info('User settings directory does not exist.  Building now.')
        makedirs(userSettings)

        logging.info('Copying default settings files.')
        copyfile('../templates/settings/' + settingsFile, userSettings + '/' + settingsFile)

    else:
        logging.info("userSettings exists.")

    if not path.isdir(userLogging):
        logging.info('Logging directory does not exist.  Building now.')
        makedirs(userLogging)
    else:
        logging.info("userLogging exists")

def cache_user_settings():
    """
    Pulls in the values set in the dbNexus.properties file.
    """

    parser = SafeConfigParser()
    settings = parser.read(userSettings + "/dbNexus.properties")



            