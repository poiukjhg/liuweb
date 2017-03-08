# -*- coding: utf-8 -*- 
class fiveelements:
	def __init__(self):
		self.names=['金','水','木','火','土']
	def get_parent(self, element):
		eindex = self.names.index(element)
		if eindex == 0:
			return self.names[4]
		return self.names[(eindex-1)%5]
	def get_child(self, element):
		eindex = self.names.index(element)
		return self.names[(eindex+1)%5]
	def get_overcomeing(self, element):
		eindex = self.names.index(element)
		return self.names[(eindex+2)%5]
	def get_overcomed(self, element):
		eindex = self.names.index(element)
		if eindex == 0:
			return self.names[3]
		if eindex == 1:
			return self.names[4]	
		return self.names[(eindex-2)%5]
	def is_overcoming(self, element1, element2):
		tmpstr = self.get_overcomeing(element1)
		if element2 == tmpstr:
			return True
		return False	
	def is_overcomed(self, element1, element2):
		tmpstr = self.get_overcomed(element1)
		if element2 == tmpstr:
			return True
		return False	
	def is_child(self, element1, element2):
		tmpstr = self.get_child(element1)
		if element2 == tmpstr:
			return True
		return False
	def is_parent(self, element1, element2):
		tmpstr = self.get_parent(element1)
		if element2 == tmpstr:
			return True
		return False


if __name__ == '__main__':
	wuxing = fiveelements();
	print ' '.join(wuxing.names)
	for index in range(5):
		print wuxing.names[index]+' :'
		print '被'+wuxing.get_parent(wuxing.names[index])+'生' \
		+ ' 生'+wuxing.get_child(wuxing.names[index]) \
		+ ' 被'+wuxing.get_overcomed(wuxing.names[index])+'克' \
		+ ' 克'+wuxing.get_overcomeing(wuxing.names[index])
