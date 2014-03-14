__author__ = 'Alex Meadows'

import wx

import gui.components.wizard.wizard
import gui.components.wizard.wizardPage as page


class NewRepoWizard():
    @staticmethod
    def create_new_repository_wizard():

        new_repo = gui.components.wizard.wizard.Wizard('Create a New Repository',
                                                       img_filename='../../../resources/images/schema.png')
        page1 = page.WizardPage(new_repo, 'Repository Details')

        page1.add_stuff(wx.StaticText(page1, -1, 'Please enter the name of the repository.\n'))

        page1.add_stuff(wx.StaticText(page1, -1, 'Repository Name'))
        page1.add_stuff(wx.TextCtrl(page1, value="", pos=(20, 60)))

        page2 = page.WizardPage(new_repo, 'Remote Setup')
        page2.add_stuff(wx.StaticText(page2, -1, 'Please enter the remote repository details.'))

        page2.add_stuff(wx.StaticText(page2, -1, "Remote Repository Name"))
        page2.add_stuff(wx.TextCtrl(page2, value="origin", pos=(20, 60)))

        page2.add_stuff(wx.StaticText(page2, -1, "Remote Repository URL"))
        page2.add_stuff(wx.TextCtrl(page2, value="git@server:repo.git", pos=(20, 60)))

        page3 = page.WizardPage(new_repo, 'Building Repository')
        page3.add_stuff(wx.StaticText(page3, -1, 'Test'))

        wx.wizard.WizardPageSimple.Chain(page1, page2)
        wx.wizard.WizardPageSimple.Chain(page2, page3)

        new_repo.run(page1)