import wx
import manager

class ListPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self,parent)
		self.mainframe = parent.GetParent()
		
		self.info = manager.GetInfo()
		
		self.titles = self.info.GetTitles()
		self.lb = wx.ListBox(self, choices = self.titles)
		self.lb.Bind(wx.EVT_LISTBOX, self.LeftMouseDown)
		self.lb.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
		
		self.del_button = wx.Button(self, -1, "Delete")
		self.Bind(wx.EVT_BUTTON, self.OnDelete, self.del_button)
		
		
		box = wx.BoxSizer(wx.VERTICAL)
		box.Add(self.lb)
		box.Add(self.del_button)
		self.SetSizer(box)
		self.Fit()
		
	def Update(self):
		self.titles = self.info.GetTitles()
		print 'titles', self.titles
		self.DisplayList()
	
	def DisplayList(self):
		self.lb.Set(self.titles)
		
	def OnKeyUp(self, e):
		code = e.GetKeyCode()
		if code == 127: #key == delete
			self.OnDelete()
			
	def LeftMouseDown(self, e):		
		entry_pos = e.GetSelection() #returns position of selection
		self.mainframe.UpdateData(entry_pos)
		return
	
	def GetSelection(self):
		return self.lb.GetSelection()
	
	def OnDelete(self, e = None):
		try:
			entry_pos = self.lb.GetSelection()
			self.mainframe.DeleteEntry(entry_pos)
		except: 
			print 'no selection for delete'
			return
		