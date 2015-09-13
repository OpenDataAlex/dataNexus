"""
Logging setup provides the configuration for custom logging, including the custom_logging levels
added in custom_logging.
"""
import logging
from os import path

from datanexus.utilities.settings_manager import SettingsManager
import datanexus.utilities.custom_logging

__author__ = 'coty', 'ameadows'

# Default application logging settings are handled thru the SettingManager.

# data_dir = SettingsManager().find_setting('')
# log_file = SettingsManager().find_setting('Logging', 'log_file')
# log_level = 'logging.' + SettingsManager().find_setting('Logging', 'log_level')

# Create the log file in the application data directory.
# log_path = path.join(data_dir, 'log', log_file)

# Create console handle and set level to application default.
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console.setFormatter(formatter)