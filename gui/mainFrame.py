__author__ = 'Alex Meadows'

import wx

import gui.wizard.wizard
import gui.wizardPage as page


objectList = {
    'schema': 'Data Source',
    'table': 'Table',
    'view': 'View',
    'index': 'Index',
    'function': 'Function/Procedure'
}


class MainFrame(wx.Frame):
    """
    The Main window for dbNexus.  Contains all user interface to the tool.
    """
    def __init__(self, parent, title):
        self.dirname = ''

        # A "-1" in the size parameter instructs wxWidgets to use the default size.
        # In this case, we select 200px width and the default height.
        wx.Frame.__init__(self, parent, title=title, size=(800, -1))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A status bar at the bottom of the window.

        #Setting up the menu.
        file_menu = wx.Menu()
        repo_menu = wx.Menu()
        about_menu = wx.Menu()

        #wx.ID_ABOUT and wx.ID_EXIT are standards IDs provided by wxWidgets
        menu_new = file_menu.Append(wx.ID_NEW, "&New", "Start a new object.")
        menu_open = file_menu.Append(wx.ID_OPEN, "&Open", "Open an object.")
        menu_exit = file_menu.Append(wx.ID_EXIT, "&Exit", "Exit the application")

        menu_new_repo = repo_menu.Append(12, "&New Repository", "Create a new repository.")

        menu_about = about_menu.Append(wx.ID_ABOUT, "&About", "Information about the program")

        #Creating the menu bar
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File") # Adding the File menu
        menu_bar.Append(repo_menu, "&Repository") #Adding the Repository menu
        menu_bar.Append(about_menu, "&Help") # Adding the Help menu
        self.SetMenuBar(menu_bar)

        # Set events
        self.Bind(wx.EVT_MENU, self.on_about, menu_about)
        self.Bind(wx.EVT_MENU, self.on_open, menu_open)
        self.Bind(wx.EVT_MENU, self.on_exit, menu_exit)
        self.Bind(wx.EVT_MENU, self.on_new, menu_new)
        self.Bind(wx.EVT_MENU, self.on_new_repo, menu_new_repo)


        #Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()

    def on_about(self, e):
        # A message dialog box with an OK button.
        dlg = wx.MessageDialog( self, "Open Source data version control and more!", "About dbNexus", wx.OK)
        dlg.ShowModal() # Show the box
        dlg.Destroy() # Finally destroy it when finished

    def on_exit(self, e):
        self.Close(True) # Close the frame.

    def on_new(self, e):
        '''
        Open dialogue for creating new objects.
        '''

        dlg = wx.ListBox(self, 26, wx.DefaultPosition, (170, 130), objectList, wx.LB_SINGLE)

        if dlg.ShowModal() == wx.ID_OK:
            self.dbObject = ''

    def on_new_repo(self, e):
        '''
        Opens dialogue for creating a new dbNexus repository.
        '''

        new_repo = gui.wizard.wizard.Wizard('Simple Wizard', img_filename='wiz.png')
        page1 = page.WizardPage(new_repo, 'Page 1')
        page1.add_stuff(wx.StaticText(page1, -1, 'Hola'))

        page2 = page.WizardPage(new_repo, 'Page 2')
        page2.add_stuff(wx.StaticText(page2, -1, 'Bonjour'))

        page3 = page.WizardPage(new_repo, 'Page 3')
        page3.add_stuff(wx.StaticText(page3, -1, 'Hiya'))

        new_repo.add_page(page1)
        new_repo.add_page(page2)
        new_repo.add_page(page3)

        wx.CallAfter(new_repo.SetSize(500, 500))

        new_repo.run()
        #new_repo.Destroy()

    def on_open(self, e):
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