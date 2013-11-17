#!/usr/bin/env python
# encoding: utf-8

import midimanager as mm
import wx


class Model(mm.Instrument):

    """represents the Waldorf Blofeld Synthesizer"""

    def __init__(self, output):
        """init """
        mm.Instrument.__init__(self, 'Blofeld', output)
        self.createParameters()

    def createParameters(self):
        """creates all Parameters and adds them
        :returns: @todo

        """
        p = mm.SynthParam('LFO1-Speed', self, 'normal', mm.CCTemplate(16))
        self.addParam(p)


class View(wx.Panel):

    """parameter panel for blofeld"""

    def __init__(self, parent):
        """@todo: to be defined1. """
        wx.Panel.__init__(self, parent)

        self.slider_LFO1S = wx.Slider
