import shelve
import myexceptions

'''
NOTE: Hard-coded key is the filename
...This could prove potentially disasterous and should probably be changed
'''

class Shelf:
	def __init__(self, filename = None):
		self.filename = filename
		self.is_open = 0
		self.operator = None
		self.key = str(self.filename)
		
	def open(self, filename = None):
		if filename is None:	
			filename = self.filename
		self.ChangeFiles(filename)
		self.operator = shelve.open(self.filename)
		self.is_open = 1
		
	def close(self):
		self.operator.close()
		self.is_open = 0
		
	def isOpen(self):
		return self.is_open
		#poor work-around... may not work if closes unexpectedly in app.
	
	def read(self, filename = None):
		if filename is None:	
			filename = self.filename
		if self.is_open == False:
			print 'file not open. opening then reading...'
			self.open(filename)
		value = self.loadKey()
		return value
		
	def write(self, value):
		self.saveKey(value)
		
	def saveKey(self, value):
		if self.isOpen() == False:
			self.open()
		try:
			self.operator[self.key] = value
		except:
			print 'shelf writing exception'
			self.operator[self.key] = 'I AM HERE THANKS TO SAVE PROBLEM'
			
	def loadKey(self):
		if self.isOpen() == False:
			self.open()
		value = None
		try:
			value = self.operator[self.key]
		except:
			print 'WARNING: shelf reading exception'
			value = 'I AM HERE BECAUSE KEY DOES NOT EXIST'
		return value
			
	def ChangeFiles(self, new_filename):
		self.filename = new_filename
		self.key = str(self.filename)