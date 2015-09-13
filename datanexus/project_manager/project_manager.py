"""
projectManager handles the creation, modification, and other project actions.
This will involve working with version control tools (primarily git) to create and maintain projects within dataNexus.
"""

__author__ = 'ameadows'

from os.path import join
from os import path, makedirs
import logging

from datanexus.project_manager.version_control.git_manager import GitManager

from datanexus.utilities.settings_manager import SettingsManager
from datanexus.utilities.logging_setup import console


class ProjectManager:
    """
    ProjectManager handles projects.
    """

    def __init__(self, project_name, project_dir, vc_type="git"):
        """
        ProjectManager requires the version control type.  By default, it's git.  Eventually other version control
        systems may be allowed, but main focus is on git.
        :param vc_type Type of version control in use by the project.
        :type vc_type: str
        :param project_name:  Name of the project.
        :type project_name: str
        :param project_dir:  Path to where the project will live
        :type project_dir: str
        """
        self.log = logging.getLogger(name='ProjectManager')
        self.log.addHandler(console)

        workspace = SettingsManager().find_setting('Locations', 'workspace')

        self.vc_type = vc_type
        self.project_name = project_name
        self.project_loc = join(workspace, project_dir)

        # Default list of directories that are built at project creation
        self.dir_list = ["table", "index", "stored_procedure", "sequence", "trigger", "view", "query"]

    def create_new_project(self):
        """
        Create a new dataNexus project based on the version control type (default git).
        :return:
        """
        # Determine if the directory is empty.
        if path.isdir(project_loc):
            self.log.info("Project directory is not empty!")

        # Based on vc_type, create the repository.

        project = GitManager().create_git_project(self.project_loc)

        for folder in self.dir_list:
            dir_path = path.join(self.project_loc, dir)
            os.makedirs(dir_path)

            #TODO:  Add blank root yaml file for listing objects.



    def open_project(self):
        """
        Opens an existing dataNexus project, within dataNexus.
        :return:
        """

        """
        Open the existing project
        """

    def close_project(self):
        """
        Closes an existing open project.
        :return:
        """

    def check_project_exists(self):
        """
        Checks to see if the project already exists, based on project_name.  Then tests to ensure that project_dir is
        empty.
        :return:
        """

    def import_project(self):
        """
        Imports existing project into dataNexus.  Will pull remote version controlled code into local.
        """

    def add_project_files(self):
        """
        Adds any missing files into version control.
        :return:
        """

    def ignore_project_files(self):
        """
        Ignores selected files from version control.
        :return:
        """

    def commit_project_files(self):
        """
        Commits files into version control.
        :return:
        """

    def push_project_files(self):
        """
        Pushes files into remote repository.
        :return:
        """

    def pull_project_files(self):
        """
        Pulls files from remote repository
        :return:
        """

    def create_project_branch(self):
        """
        Creates new project branch from a selected branch.
        :return:
        """

    def merge_project_branch(self):
        """
        Merges the current branch into a selected branch.
        :return:
        """

