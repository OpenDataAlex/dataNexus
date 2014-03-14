__author__ = 'Alex Meadows'

import git

from utils.settingsManager import userSettings


class Repository:
    def __init__(self, name):
        self.name = None

    def create_repo(self, name, remote, url):


        git.Repo.init(userSettings/name, bare=True)
        git.Repo.create_remote(remote, url)

    def edit_repo(self, repo):
        print ''

    def delete_repo(self, repo):
        print ''

    def pull_repo(self, name, remote):
        print ''

    def push repo(self, name, remote):
        print ''

    def fetch_repo(self, name, remote):
        print ''