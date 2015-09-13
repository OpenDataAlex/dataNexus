"""
GitManager handles all functionality with Git.  This is designed so that other version control tools can be utilized
with minimum re-work of the project manager class.
"""
from git import Repo
import logging
from datanexus.utilities.logging_setup import console

__author__ = 'ameadows'


class GitManager:

    def __init__(self):

        self.log = logging.getLogger(name='GitManager')
        self.log.addHandler(console)

    def create_git_project(self, project_dir, bare=True):
        """
        Creates a project using Git as the version control tool.
        :param project_dir:  Filepath to the project directory.
        :type project_dir:  string
        :param bare:  Should the initial directory be bare?  Default true
        :return:  git project instance
        """
        self.log.info("Creating project at {0:s}".format(project_dir))

        return Repo.init(project_dir, bare)
