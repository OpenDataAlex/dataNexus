"""
Main window class for dataNexus.  Acts as the main interface for the application.
"""

__author__ = 'ameadows'


import sys
import logging
from PySide.QtGui import QMainWindow, QApplication, QWidget, QLabel, QAction

from datanexus.gui.menu import Menu

class MainWindow(QMainWindow):
    """
    Creates the main window for dataNexus.  Also handles any functions for the main window.
    """
    def __init__(self):
        """
        Initializes the application and logging for the MainWindow class.
        """
        self.app = QApplication(sys.argv)

    def create_main_window(self, version):
        """
        Creates the main application window and returns it.
        :param version: The application's version number, found in the project root-level __init__.py
        :return:
        """

        window = QMainWindow()
        window.setMinimumSize(800, 600)
        window.setWindowTitle("dataNexus v" + version)

        # Create the menu for main window.
        menu = window.menuBar()

        sub_menus = Menu(menu, window)

        sub_menus.create_file_menu()
        sub_menus.create_edit_menu()
        sub_menus.create_about_menu()

        window.show()

        self.app.exec_()


