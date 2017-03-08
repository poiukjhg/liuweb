# -*- coding: utf-8 -*- 
class output_results():
	def __init__(self, skytrunk, earthbranch, monthgeneral, fortell_hour, skyplate, skygeneral, fourclass_buttom, fourclass_upper, triline):
		self.skytrunk = skytrunk
		self.earthbranch = earthbranch
		self.fortell_hour = fortell_hour
		self.monthgeneral = monthgeneral
		self.skyplate = skyplate
		self.skygeneral = skygeneral
		self.fourclass_upper = fourclass_upper
		self.fourclass_buttom = fourclass_buttom
		self.triline = triline
	#	self.trisshift = trisshift
	def output(self):
		tmpline = ''
		tmpline = tmpline+'<p>'
		tmpline = tmpline+ self.skytrunk+self.earthbranch+'日'+self.fortell_hour+'时'+self.monthgeneral+'将'+'</p><p>'
		tmpline = tmpline+ '&nbsp&nbsp&nbsp&nbsp'+self.skygeneral[5]+'&nbsp&nbsp'+self.skygeneral[6]+'&nbsp&nbsp'+self.skygeneral[7]+'&nbsp&nbsp'+self.skygeneral[8]+'&nbsp&nbsp'+'</p><p>'	
		tmpline = tmpline+ '&nbsp&nbsp&nbsp&nbsp'+self.skyplate[5]+'&nbsp&nbsp'+self.skyplate[6]+'&nbsp&nbsp'+self.skyplate[7]+'&nbsp&nbsp'+self.skyplate[8]+'&nbsp&nbsp'+'</p><p>'	
		tmpline = tmpline+ '&nbsp'+self.skygeneral[4]+self.skyplate[4]+'&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp'+self.skyplate[9]+self.skygeneral[9]+'</p><p>'
		tmpline = tmpline+ '&nbsp'+self.skygeneral[3]+self.skyplate[3]+'&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp'+self.skyplate[10]+self.skygeneral[10]+'</p><p>'
		tmpline = tmpline+ '&nbsp&nbsp&nbsp&nbsp'+self.skyplate[2]+'&nbsp&nbsp'+self.skyplate[1]+'&nbsp&nbsp'+self.skyplate[0]+'&nbsp&nbsp'+self.skyplate[11]+'&nbsp&nbsp'+'</p><p>'			
		tmpline = tmpline+ '&nbsp&nbsp&nbsp&nbsp'+self.skygeneral[2]+'&nbsp&nbsp'+self.skygeneral[1]+'&nbsp&nbsp'+self.skygeneral[0]+'&nbsp&nbsp'+self.skygeneral[11]+'&nbsp&nbsp'+'</p><p>'	
		tmpline = tmpline+ ''+'</p><p>'
		tmpline = tmpline+ '四课：'+'</p><p>'
		tmpgeneral = ['','','','']
		for index in range(4):
			tmpgeneral[index] = self.skygeneral[self.skyplate.index(self.fourclass_upper[3-index])]
		tmpline = tmpline+ tmpgeneral[0]+'&nbsp&nbsp'+tmpgeneral[1]+'&nbsp&nbsp'+tmpgeneral[2]+'&nbsp&nbsp'+tmpgeneral[3]+'&nbsp&nbsp'+'</p><p>'
		tmpline = tmpline+ self.fourclass_upper[3]+'&nbsp&nbsp'+self.fourclass_upper[2]+'&nbsp&nbsp'+self.fourclass_upper[1]+'&nbsp&nbsp'+self.fourclass_upper[0]+'&nbsp&nbsp'+'</p><p>'
		tmpline = tmpline+ self.fourclass_buttom[3]+'&nbsp&nbsp'+self.fourclass_buttom[2]+'&nbsp&nbsp'+self.fourclass_buttom[1]+'&nbsp&nbsp'+self.fourclass_buttom[0]+'&nbsp&nbsp'+'</p><p>'
		tmpline = tmpline+ self.triline+'</p>'
		return tmpline
