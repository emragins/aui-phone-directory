import wx
import info
import textvalidator
import manager


class EditPanel(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent)
		self.mainframe = parent.GetParent()
		self.info = manager.GetInfo()
		
		self.textbox = []
		
		#Initialize notice texts
		self.notice_text = None
		
		#create layout
		self.gbs = wx.GridBagSizer(7,6)
		self.CreateInteriorComponents()
		self.Add()
		self.gbs.Layout()

	def Add(self):
		box = wx.BoxSizer()
		box.Add(self.gbs, 0, wx.ALL, 20)
	
		self.SetSizerAndFit(box)
		self.SetClientSize(self.GetSize())
		
	def CreateInteriorComponents(self):
		self.CreateLabels()
		self.CreateTextFields()
		self.CreateButtons()		
		#self.CreateNotices()
		
	def CreateLabels(self):
		self.gbs.Add(wx.StaticText(self, -1, "First Name"), (1,1))
		self.gbs.Add(wx.StaticText(self, -1, "Last Name"), (2,1))
		self.gbs.Add(wx.StaticText(self, -1, "Home Number"), (3,1))
		self.gbs.Add(wx.StaticText(self, -1, "Cell Number"), (4,1))
		self.gbs.Add(wx.StaticText(self, -1, "Work Number"), (5,1))
		
	def CreateTextFields(self):
		textboxdata = [[self, -1, "", textvalidator.NameValidator()],
					[self, -1, "", textvalidator.NameValidator()],
					[self, -1, "", textvalidator.PhoneNumberValidator()],
					[self, -1, "", textvalidator.PhoneNumberValidator()],
					[self, -1, "", textvalidator.PhoneNumberValidator()]]
					
		textbox = self.textbox
		for i in textboxdata:
			textbox.append(wx.TextCtrl(i[0], i[1], i[2], validator = i[3]))
		
		self.gbs.Add(textbox[0], (1,2))
		self.gbs.Add(textbox[1], (2,2))
		self.gbs.Add(textbox[2], (3,2))
		self.gbs.Add(textbox[3], (4,2))
		self.gbs.Add(textbox[4], (5,2))
		
		
	def CreateButtons(self):
		but_store = wx.Button(self, -1, "Store")
		but_new = wx.Button(self, -1, "New Entry")
		self.gbs.Add(but_store, (6,1))
		self.gbs.Add(but_new, (6,2))
		
		self.Bind(wx.EVT_BUTTON, self.OnStore, but_store)
		self.Bind(wx.EVT_BUTTON, self.OnNew, but_new)
	'''
	def CreateNotices(self):
		self.gbs.AddGrowableRow(8)
		self.notice_text = wx.StaticText(self, -1, self.notice_text_value)
		self.gbs.Add(self.notice_text, (8,1))
		self.gbs.Hide(self.notice_text)
	'''
	
	def Update(self, entry_pos):
		entry_data = self.info.GetRowWithoutTitle(entry_pos)
		count = 0
		for tb in self.textbox:
			tb.SetValue(entry_data[count])
			count += 1
			
#--------EVENT HANDLING INTERFACE--------------------------------------------------------				
	def IsNumber(self, e):
		str = e.GetSring()
		str_len = len(Str)
		
	def OnStore(self, e):
		#values initialized as a place holder for 'title'
		values = [1]
		values[0] = ''
		
		#pull data and add to info
		for i in self.textbox:
			datastring = i.GetValue()
			values.append(datastring)
		
		self.info.AddEntry(values)
		self.mainframe.EntryAdded()
	
	''' 
	BIG MESS ->
	
	def EntryEmpty(self):
		self.gbs.Show(self.notice_text_value['empty'])
		self.gbs.Layout()
		manager.wait(200)
		self.gbs.Hide(self.notice_text)
		self.gbs.Layout()
	'''
	
	def OnNew(self, e = None):
		for i in self.textbox:
			i.Clear()
			
	