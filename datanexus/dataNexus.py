"""
This is the primary entry point to access Data Nexus.
"""

__author__ = 'ameadows'


from datanexus.utilities.settings_manager import SettingsManager
from datanexus.gui.main_window import MainWindow
from datanexus import __version__
def main():
    """
    Load up background processes (TO DO) and open the primary window.
    :return:
    """

    MainWindow().create_main_window(__version__)

if __name__ == '__main__':
    #SettingsManager.first_run_test()
    main()