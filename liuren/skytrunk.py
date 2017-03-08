# -*- coding: utf-8 -*- 
class skytrunk():
	def __init__(self):
		self.names =         [ '甲','乙','丙','丁','戊','己','庚','辛','壬','癸' ]
		self.attribute =     [ '木','木','火','火','土','土','金','金','水','水' ]
		self.cooperation =   [ '己','庚','辛','壬','癸','甲','乙','丙','丁','戊' ]
		self.stoeb =         [ '寅','辰','巳','未','巳','未','申','戌','亥','丑' ]	
		self.yinyang =       [ '阳','阴','阳','阴','阳','阴','阳','阴','阳','阴' ]	
	def get_attribute(self, element):
		eindex = self.names.index(element)
		return self.attribute[eindex]
	def get_cooperation(self, element):
		eindex = self.names.index(element)
		return self.cooperation[eindex]