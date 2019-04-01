# -*- coding: utf-8 -*- 
#  noname.py
###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import time     #new

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Milo Chat", pos = wx.DefaultPosition, size = wx.Size( 412,325 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"All Aontents", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText3.Wrap( -1 )
		bSizer1.Add( self.m_staticText3, 0, wx.EXPAND, 5 )
		
		self.allText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer1.Add( self.allText, 1, wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"I SAY", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText4.Wrap( -1 )
		bSizer1.Add( self.m_staticText4, 0, wx.EXPAND, 5 )
		
		self.textIn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer1.Add( self.textIn, 0, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnSent = wx.Button( self, wx.ID_ANY, u"Sent", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btnSent, 0, wx.ALL, 5 )
		
		self.btnClear = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btnClear, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer6, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnSent.Bind( wx.EVT_BUTTON, self.OnButtonSent )
		self.btnClear.Bind( wx.EVT_BUTTON, self.OnButtonClear )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonSent( self, event ):
		event.Skip()
		"""new"""
		userinput = self.textIn.GetValue()
		self.textIn.Clear()
		nowtime = time.ctime()
		inmsg = "You (%s) :\n%s \n" % (nowtime,userinput)
		self.allText.AppendText(inmsg)
		
	
	def OnButtonClear( self, event ):
		event.Skip()
	
if __name__ == "__main__":    #new
        app = wx.App()
        frame = MyFrame2(None)
        frame.Show()
        app.MainLoop()   
