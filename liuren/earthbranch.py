# -*- coding: utf-8 -*- 
class earthbranch:
	def __init__(self):
		self.names =       ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
		self.attribute =   ['水','土','木','木','土','火','火','土','金','金','土','水']
		self.opposited =   ['午','未','申','酉','戌','亥','子','丑','寅','卯','辰','巳']
		self.cooperation = ['丑','子','亥','戌','酉','申','未','午','巳','辰','卯','寅']
		self.xing =        ['卯','戌','巳','子','辰','申','午','丑','寅','酉','未','亥']
		self.hai =         ['未','午','巳','辰','卯','寅','丑','子','亥','戌','酉','申']
		self.yinyang =     ['阳','阴','阳','阴','阳','阴','阳','阴','阳','阴','阳','阴']	
		self.tricoop =     [['申','子','辰'],['巳','酉','丑'],['寅','午','戌'],['亥','卯','未'],['申','子','辰'],['巳','酉','丑'], \
							['寅','午','戌'],['亥','卯','未'],['申','子','辰'],['巳','酉','丑'],['寅','午','戌'],['亥','卯','未']]
	def get_earthbranch_names(self):
		return self.names	
	def get_attribute(self, element):
		eindex = self.names.index(element)
		return self.attribute[eindex]
	def get_opposited(self, element):
		eindex = self.names.index(element)
		return self.opposited[eindex]
	def get_cooperation(self, element):
		eindex = self.names.index(element)
		return self.cooperation[eindex]
	def get_xing(self, element):
		eindex = self.names.index(element)
		return self.xing[eindex]
	def get_hai(self, element):
		eindex = self.names.index(element)
		return self.hai[eindex]
	def get_tricoop(self, element):
		eindex = self.names.index(element)
		return self.tricoop[eindex]
