__author__ = 'ameadows'
'''
The main script for dbNexus.
Starts by creating a splash screen that shows the loading status
then returns the main window of the GUI.
'''

import wx

from gui.mainFrame import MainFrame

def show_splash():
    global splash
    bitmap = wx.Image(name='./resources/images/dbnexusSplash.png').ConvertToBitmap()
    splash = wx.SplashScreen(bitmap, wx.SPLASH_CENTRE_ON_SCREEN|wx.SPLASH_NO_TIMEOUT, 0, None, -1)
    splash.Show()
    return splash


def main():
    app = wx.App(False)
    splash = show_splash()

    # do processing/initialization here and create main window
    frame = MainFrame(None, title='dbNexus')
    frame.Show()

    splash.Destroy()
    app.MainLoop()

if __name__ == '__main__':
    main()