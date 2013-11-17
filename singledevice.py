#!/usr/bin/env python
# encoding: utf-8


import wx
import midimanager as mm


class Controller(object):

    """controller class"""

    def __init__(self, app):
        """@todo: to be defined1. """
        self.model = mm.Rack('Singledevice')
        self.main = Mainframe(None, -1, 'singledevice')
        self.main.Show(True)


class Mainframe(wx.Frame):

    """main frame"""

    def __init__(self, parent, id, title):
        """@todo: to be defined1.

        :parent: @todo
        :id: @todo
        :title: @todo

        """
        wx.Frame.__init__(self, parent, id, title)

        menubar = wx.MenuBar()
        file = wx.Menu()
        file.Append(101, '&Quit', 'Quit Application')
        device = wx.Menu()
        device.Append(201, '&New', 'Create new Device')

        menubar.Append(file, '&File')
        menubar.Append(device, '&Devices')
        self.SetMenuBar(menubar)
        self.CreateStatusBar()


if __name__ == '__main__':
    app = wx.App(False)
    controller = Controller(app)
    app.MainLoop()
