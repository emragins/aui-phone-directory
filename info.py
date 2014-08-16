
"""
entry = 
0: name for tree
1: first name
2: last name
3: home number
4: cell number
5: work number
6: e-mail address -- not right now
"""

class Info:
	def __init__(self, entries = []):
		
		self.entries = entries
		
	def GetFullList(self):
		return self.entries
	
	def GetRowWithoutTitle(self, pos):
		r = self.entries[pos][1:]
		return r
	
	def GetTitles(self):
		titles = []
		for n in self.entries:
			titles.append(n[0])
		return titles
	
	def AddEntry(self, entry):
		title = self.MakeTitle(entry)
		new = self.VerifyNewEntry(title)
		entry[0] = title
		if new == False:
			count = 0
			for e in self.entries:
				if title == e[0]:
					self.entries[count] = entry
					break
				count += 1
		else:
			self.entries.append(entry)
			
			
	def DeleteEntry(self, row_num):
		self.entries.pop(row_num)
	
	def MakeTitle(self, entry):
		if entry[2] != '':
			str = entry[2] + ', ' + entry[1]
		else:
			str = entry[1]
		return str
	
	def VerifyNewEntry(self, title):
		for e in self.entries:
			if e[0] == title:
				return False
		return True
	
	def Sort(self):
		self.entries.sort()
	
	def __str__(self):
		if self.entries == None:
			return 'Info object "entries" is empty'
		else: return str(self.entries)