__author__ = 'ameadows'

import wx

class MainFrame(wx.Frame):
    """
    The Main window for dbNexus.  Contains all user interface to the tool.
    """
    def __init__(self, parent, title):
        self.dirname=''

        # A "-1" in the size parameter instructs wxWidgets to use the default size.
        # In this case, we select 200px width and the default height.
        wx.Frame.__init__(self, parent, title=title, size=(200, -1))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A statusbar at the bottom of the window.

        #Setting up the menu.
        filemenu = wx.Menu()

        #wx.ID_ABOUT and wx.ID_EXIT are standards IDs provided by wxWidgets
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open a file.")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Information about the program")
        menuExit = filemenu.Append(wx.ID_EXIT, "&Exit", "Exit the application")

        #Creating the menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File") # Adding the File menu
        self.SetMenuBar(menuBar)

        # Set events
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0,6):
            self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

        #Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()

    def OnAbout(self, event):
        # A message dialog box with an OK button.
        dlg = wx.MessageDialog( self, "Testing", "About dbNexus", wx.OK)
        dlg.ShowModal() # Show the box
        dlg.Destroy() # Finally destroy it when finished

    def OnExit(self, e):
        self.Close(True) # Close the frame.

    def OnOpen(self, e):
        """
        Open a file
        """
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()