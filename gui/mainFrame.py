__author__ = 'Alex Meadows'

import wx

import repository.newRepositoryWizard as new_repo_wizard


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
    def __init__(self, parent, id=wx.ID_ANY, title="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE,
                 name="MainFrame"):

        super(MainFrame, self).__init__(parent, id, title,
                                        pos, size, style, name)

        #Attributes
        self.panel = wx.Panel(self)
        self.dirname = ''

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
        menu_bar.Append(file_menu, "&File")  # Adding the File menu
        menu_bar.Append(repo_menu, "&Repository")  # Adding the Repository menu
        menu_bar.Append(about_menu, "&Help")  # Adding the Help menu
        self.SetMenuBar(menu_bar)

        # Set events
        self.Bind(wx.EVT_MENU, self.on_about, menu_about)
        self.Bind(wx.EVT_MENU, self.on_open, menu_open)
        self.Bind(wx.EVT_MENU, self.on_exit, menu_exit)
        self.Bind(wx.EVT_MENU, self.on_new, menu_new)
        self.Bind(wx.EVT_MENU, self.on_new_repo, menu_new_repo)

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

    @staticmethod
    def on_new_repo(self):
        '''
        Opens dialogue for creating a new dbNexus repository.
        '''

        repo_types = [
            "Git",
            "Subversion"
        ]

        new_repo_wizard.NewRepoWizard.create_new_repository_wizard()


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