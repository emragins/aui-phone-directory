# Nearly all this code is taken from the wxPython demo

import wx
import string

class PhoneNumberValidator(wx.PyValidator):
	def __init__(self, pyVar = None):
		wx.PyValidator.__init__(self)
		self.Bind(wx.EVT_CHAR, self.OnChar)

	def Clone(self):
		return PhoneNumberValidator()

	def Validate(self, win):
		print 'validate'
		tc = self.GetWindow()
		val = tc.GetValue()
        
		for x in val:
			if x not in string.digits:
				return False

		return True


	def OnChar(self, event):
		key = event.GetKeyCode()
		
		if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:
			event.Skip()
			return
		
		elif key is 45:
			event.Skip()
			return

		
		elif chr(key) in string.digits:
			event.Skip()
			return

		elif not wx.Validator_IsSilent():
			wx.Bell()
		
		# Returning without calling even.Skip eats the event before it
		# gets to the text control
		return

class NameValidator(wx.PyValidator):
	def __init__(self):
		wx.PyValidator.__init__(self)
		