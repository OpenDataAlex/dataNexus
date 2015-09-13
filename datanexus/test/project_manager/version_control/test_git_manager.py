"""
This module is for testing the GitManager, part of the project manager component.
"""

__author__ = 'ameadows'

import unittest
import os
import shutil

from datanexus.project_manager.version_control.git_manager import GitManager


class GitManagerTests(unittest.TestCase):
    """
    We first have to set up some paramters that will be utilized by the GitManager methods.
    """

    def setUp(self):
        #TODO:  Change to use SettingsManager.
        self.project_dir = "/home/ameadows/datanexus/project1"
        self.git_dir = os.path.join(self.project_dir, '.git')

    def test_create_git_project(self):
        """
        Testing the creation of a project directory using git for version control.
        :return:
        """
        # Verify the directory does not exist beforehand
        self.assertFalse(os.path.isdir(self.git_dir))

        project = GitManager().create_git_project(self.project_dir)

        # Verify the directory and project is created
        self.assertTrue(os.path.isdir(self.git_dir))

        # Clean up directory once test is complete
        shutil.rmtree(self.project_dir)
