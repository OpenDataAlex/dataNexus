__author__ = 'Alex Meadows'
"""
Code is based on example provided in the wxPython docs.
"""
from os import path

import wx
import wx.wizard as wizmod


class Wizard(wx.wizard.Wizard):
    '''
      Creating wizard class for processes that need more of a walk through.
    '''

    def __init__(self, title, img_filename=""):
        if img_filename and path.exists(img_filename):
            img = wx.Bitmap(img_filename)
        else:
            img = wx.NullBitmap

        wx.wizard.Wizard.__init__(self, None, -1, title, img)

        self.pages = []
        self.Bind(wizmod.EVT_WIZARD_PAGE_CHANGED, self.on_page_changed)
        self.Bind(wizmod.EVT_WIZARD_PAGE_CHANGING, self.on_page_changing)
        self.Bind(wizmod.EVT_WIZARD_CANCEL, self.on_cancel)
        self.Bind(wizmod.EVT_WIZARD_FINISHED, self.on_finished)

    def add_page(self, page):
        '''
        Add a wizard page to the list.
        '''

        if self.pages:
            previous_page = self.pages[-1]
            page.set_prev(previous_page)
            previous_page.set_next(page)

        self.pages.append(page)

    def run(self, page):
        self.RunWizard(page)

    def on_page_changed(self, evt):
            '''
            Executed after the page has changed.
            '''

            if evt.GetDirection():
                dir = "forward"
            else:
                dir = "backward"

            page = evt.GetPage()
            print "page_changed: %s, %s\n" % (dir, page.__class__)

    def on_page_changing(self, evt):
        '''
        Executed before the page changes, so we might veto it.
        '''

        if evt.GetDirection():
            dir = "forward"
        else:
            dir = "backward"

        page = evt.GetPage()

        print "page_changing: %s, %s\n" % (dir, page.__class__)

    def on_cancel(self, evt):
        '''
        Cancel button has been pressed.  Clean up and exit without continuing.
        '''

        page = evt.GetPage()
        print "on_cancel: %s\n" % page.__class__

        #Prevent cancelling of the wizard.
        if page is self.pages[0]:
            wx.MessageBox("Cancelling on the first page has been prevented.", "Sorry")
            evt.Veto()

    def on_finished(self, evt):
        '''
        Finish button has been pressed.  Clean up and exit.
        '''

        print "OnWizFinished\n"
