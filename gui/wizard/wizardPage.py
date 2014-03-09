__author__ = 'Alex Meadows'
"""
Code is based on example provided in the wxPython docs.
"""
import wx
import wx.wizard as wizmod
padding = 5


class WizardPage(wizmod.PyWizardPage):
    '''
    An extended panel obj with a few methods to keep track of its siblings.
    '''

    def __init__(self, parent, title):
        wx.wizard.PyWizardPage.__init__(self, parent)
        self.next = self.prev = None
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(self, -1, title)
        title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))

        self.sizer.AddWindow(title, 0, wx.ALIGN_LEFT | wx.ALL, padding)
        self.sizer.AddWindow(wx.StaticLine(self, -1), 0, wx.EXPAND | wx.ALL, padding)
        self.SetSizer(self.sizer)

    def add_stuff(self, stuff):
        '''
        Add additional widgets to the bottom of the page.
        '''

        self.sizer.Add(stuff, 0, wx.EXPAND | wx.ALL, padding)

    def set_next(self, page):
        '''
        Set the next page.
        '''
        self.next = page

    def set_prev(self, page):
        '''
        Set the previous page
        '''
        self.prev = page

    def get_next(self):
        '''
        Return the next page
        '''

        return self.next

    def get_prev(self):
        '''
        Return the previous page
        '''

        return self.prev

