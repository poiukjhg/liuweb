# -*- coding: utf-8 -*- 
import skytrunk
import earthbranch
class skygeneral:
	def __init__(self):
		self.fullnames = ['贵人','螣蛇','朱雀','六合','勾陈','青龙','天空','白虎','太常','玄武','太阴','天后']
		self.names = 	 ['贵',  '蛇',   '雀', '合',  '勾',   '龙',  '空',  '虎',  '常',  '玄',  '阴',  '后']		
		#                    ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
		self.day_god_loc =   ['丑','子','亥','亥','丑','子','丑','午','巳','巳']
		self.night_god_loc = ['未','申','酉','酉','未','申','未','寅','卯','卯']
	def get_full_names(self, element):
		return self.fullnames[self.names.index(element)]
	def get_god_loc(self, today_st, foretell_hour):
		skt = skytrunk.skytrunk()
		etb = earthbranch.earthbranch()
		skt_index = skt.names.index(today_st)
		etb_index = etb.names.index(foretell_hour)
		if etb_index > 2 and etb_index < 9:
			return self.day_god_loc[skt_index]
		else:
			return self.night_god_loc[skt_index]
	def get_skygeneral_list(self, today_st, skyplate, foretell_hour):
		skygeneral_list = ['贵',  '蛇',   '雀', '合',  '勾',   '龙',  '空',  '虎',  '常',  '玄',  '阴',  '后']		
		etb = earthbranch.earthbranch()
		god_loc = self.get_god_loc(today_st, foretell_hour)
		#print "贵人在"+god_loc
		sky_shift = skyplate.index('子')
		god_etb_index = (etb.names.index(god_loc)+sky_shift)%12
		#print "贵人在地盘"+etb.names[god_etb_index]	
		if god_etb_index>4 and god_etb_index<11:
			#print "逆序"
			for index in range(12):	
				skygeneral_list[(index+god_etb_index)%12] = self.names[(12-index)%12] 
		else:	
			#print "顺序"	
			for index in range(12):	
				skygeneral_list[(index+god_etb_index)%12] = self.names[index] 					
		return skygeneral_list	


