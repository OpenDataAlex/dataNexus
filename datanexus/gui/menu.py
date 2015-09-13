"""
Menu handles the menu for dataNexus, including all submenus.
"""

__author__ = 'ameadows'

from PySide.QtGui import QMenu, QAction

class Menu:
    """
    Creates the sub-menus for the main window's menu-bar.
    """

    def __init__(self, menu, window):
        """
        :param menu: The main window menu.
        :param window: The main window object.
        """
        self.menu = menu
        self.window = window

    def create_file_menu(self):
        """
        Creates the sub-menu for the File menu.

        :return: file_menu:  File menu with revised actions.
        """
        file_menu = self.menu.addMenu("File")

        # Create project allows for new project creation.
        create_project_action = QAction("Create Project", )

        # The way to quit the application from the File menu.
        exit_action = QAction("Exit", self.window)
        exit_action.triggered.connect(exit)


        file_menu.addAction(exit_action)

        return file_menu

    def create_edit_menu(self):
        """
        Creates the sub-menu for the Edit menu.
        :return: edit_menu:  Edit menu with revised actions.
        """
        edit_menu = self.menu.addMenu("Edit")

        return edit_menu

    def create_about_menu(self):
        """
        Creates the sub-menu for the About menu.
        :return: about_menu: About menu with revised actions.
        """

        about_menu = self.menu.addMenu("About")

        return about_menu
