# -*- coding: utf-8 -*- 
import fiveelements
import earthbranch
import skytrunk
import os, sys
import global_record_list
class trishift:
	def __init__(self, upperlist, bottomlist, skyplate, skygeneral, skyplate_st):		
		self.eb_instance = earthbranch.earthbranch()
		self.st_instance = skytrunk.skytrunk()
		self.fe_instance = fiveelements.fiveelements()
		self.skyplate = skyplate
		self.skyplate_st = skyplate_st
		self.skygeneral = skygeneral
		self.upperlist = upperlist
		self.bottomlist = bottomlist
		self.up_bottom_overcome = [0]*4
		self.up_bottom_overcome_yao = [0]*4
		self.bottom_attri = ['']*4
		self.upper_attri = ['']*4
		self.ninefunc = ''
		self.tri = ['']*3
		self.out_lines = ''
	def build_trishift(self):	
		self.upper_attri = list(map(lambda x: self.eb_instance.attribute[self.eb_instance.names.index(x)], self.upperlist))	
		self.bottom_attri[0] = self.st_instance.attribute[self.st_instance.names.index(self.bottomlist[0])]
		self.bottom_attri[1:] = list(map(lambda x: self.eb_instance.attribute[self.eb_instance.names.index(x)], self.bottomlist[1:]))		
		print '  '.join(self.upper_attri[::-1])
		print '  '.join(self.bottom_attri[::-1])
		for index in range(4):
			#贼
			if self.fe_instance.is_overcoming(self.bottom_attri[index], self.upper_attri[index]):
				self.up_bottom_overcome[index] = 1
			#克	
			if self.fe_instance.is_overcomed(self.bottom_attri[index], self.upper_attri[index]):
				self.up_bottom_overcome[index] = 2	
			
		print '  '.join(list(map(lambda x:['  ', '贼','克'][x], self.up_bottom_overcome[::-1])))
		today_stoeb = self.st_instance.stoeb[self.st_instance.names.index(self.bottomlist[0])]	
		print '日干寄宫'+today_stoeb		
		full_four = (len(self.upperlist)==len(set(self.upperlist)))	
		'''
		if self.bottomlist[0] == '戊' and self.bottomlist[2] == '辰' and self.upperlist[0] == '子':
			self.spec(1)
			return self.out_lines
		'''	
		if self.bottomlist[0] =='戊' and self.bottomlist[2] == '辰' and self.upperlist[2] == '戌':
			self.spec(2)
			return self.out_lines
		if self.bottomlist[0]== '戊' and self.bottomlist[2] == '戌' and self.upperlist[2] == '辰':
			self.spec(2)
			return self.out_lines				
		if full_four == False:
			print '不备'					
			#伏吟
			if self.upperlist[0] == today_stoeb: 
				self.ninefunc = "伏吟"
				self.fuyin()
				return self.out_lines					
		#重审
		if self.up_bottom_overcome.count(1) == 1 :
			self.ninefunc = "重审"
			self.haske(self.up_bottom_overcome.index(1))
			return self.out_lines	
		if 	self.up_bottom_overcome.count(1) > 1:
			stattr = self.st_instance.yinyang[self.st_instance.names.index(self.bottomlist[0])]
			same_attr = [0]*4
			for index in range(4):
				if self.up_bottom_overcome[index] == 1:					
					tmpyinyang = self.eb_instance.yinyang[self.eb_instance.names.index(self.upperlist[index])]
					print stattr +tmpyinyang
					if tmpyinyang == stattr:
						same_attr[index] = 1
			#比用	
			print "阴阳相比 "+str(same_attr.count(1))
			if same_attr.count(1) == 1 or (self.bottomlist[2] == today_stoeb and same_attr.count(1) == 2) :
				self.ninefunc = "比用"		
				self.haske(same_attr.index(1))	
			else:
			#涉害	
			#直接使用孟仲季的取法，排除戊辰日特例即可
				self.ninefunc = "涉害"	
				sehai = ['']*4
				tmpindex = -1
				for index in range(4):
					if self.up_bottom_overcome[index]  == 1:
						if index == 0:
							tmpstr = today_stoeb
						else:
							tmpstr = self.bottomlist[index]						
						ltmpindex = self.eb_instance.names.index(tmpstr)												
						ltmpindex = self.eb_instance.tricoop[ltmpindex].index(tmpstr)
						sehai[index] = ['孟', '仲', '季'][ltmpindex]
						print self.bottomlist[index]+' 涉害 '+sehai[index]
				if sehai.count('孟') == 1:
					tmpindex = sehai.index('孟')
				elif sehai.count('孟') == 0 and sehai.count('仲') == 1:
					tmpindex = sehai.index('仲')
				elif sehai.count('孟') == 0 and sehai.count('仲') == 0 and sehai.count('季') == 1:
					tmpindex = sehai.index('季')															
				if (sehai.count('孟') >1) or (sehai.count('孟')== 0 and sehai.count('仲') > 1) or (sehai.count('孟') == 0 and sehai.count('仲') == 0 and sehai.count('季') > 1):
					if stattr == '阳':
						if self.up_bottom_overcome[0] == 1:
							tmpindex = 0	
						else:
							tmpindex = 1								
					else:
						if self.up_bottom_overcome[2] == 1:
							tmpindex = 2	
						else:
							tmpindex = 3
				if 	tmpindex == -1:
					print '涉害 error'
					return None
				self.haske(tmpindex)		
			return self.out_lines
		#元首
		if self.up_bottom_overcome.count(2) == 1:
			self.ninefunc = "元首"
			self.haske(self.up_bottom_overcome.index(2))
			return self.out_lines			
		if self.up_bottom_overcome.count(2) >1:
			stattr = self.st_instance.yinyang[self.st_instance.names.index(self.bottomlist[0])]
			same_attr = [0]*4
			for index in range(4):
				if self.up_bottom_overcome[index] == 2:
					tmpyinyang = self.eb_instance.yinyang[self.eb_instance.names.index(self.upperlist[index])]
					print stattr +tmpyinyang
					if tmpyinyang == stattr:
						same_attr[index] = 1
			print "阴阳相比 "+str(same_attr.count(1))			
			#比用			
			if same_attr.count(1) == 1 or (self.bottomlist[2] == today_stoeb and same_attr.count(1) == 2) :
				self.ninefunc = "比用"		
				self.haske(same_attr.index(1))	
			else:
			#涉害	
			#直接使用孟仲季的取法，排除戊辰日特例即可
				self.ninefunc = "涉害"
				sehai = ['']*4
				tmpindex = -1
				for index in range(4):
					if self.up_bottom_overcome[index]  == 2:
						if index == 0:
							tmpstr = today_stoeb
						else:
							tmpstr = self.bottomlist[index]	
						ltmpindex = self.eb_instance.names.index(tmpstr)												
						ltmpindex = self.eb_instance.tricoop[ltmpindex].index(tmpstr)
						sehai[index] = ['孟', '仲', '季'][ltmpindex]
						print self.upperlist[index]+' 涉害 '+sehai[index]
				if sehai.count('孟') == 1:
					tmpindex = sehai.index('孟')
				elif sehai.count('孟') == 0 and sehai.count('仲') == 1:
					tmpindex = sehai.index('仲')
				elif sehai.count('孟') == 0 and sehai.count('仲') == 0 and sehai.count('季') == 1:
					tmpindex = sehai.index('季')															
				if (sehai.count('孟') >1) or (sehai.count('孟')== 0 and sehai.count('仲') > 1) or (sehai.count('孟') == 0 and sehai.count('仲') == 0 and sehai.count('季') > 1):
					if stattr == '阳':
						if self.up_bottom_overcome[0] == 2:
							tmpindex = 0	
						else:
							tmpindex = 1								
					else:
						if self.up_bottom_overcome[2] == 2:
							tmpindex = 2	
						else:
							tmpindex = 3
						tmpindex = 2	
				if 	tmpindex == -1:
					print '涉害 error'
					return None
				self.haske(tmpindex)										
			return self.out_lines
		#遥克
		for index in range(4):
			#弹
			if self.fe_instance.is_overcoming(self.bottom_attri[0], self.upper_attri[index]):
				self.up_bottom_overcome_yao[index] = 3
			#蒿	
			if self.fe_instance.is_overcomed(self.bottom_attri[0], self.upper_attri[index]):
				self.up_bottom_overcome_yao[index] = 4
		print '  '.join(list(map(lambda x:['  ', '贼','克', '弹', '矢'][x], self.up_bottom_overcome_yao[::-1])))
		#蒿矢	
		if self.up_bottom_overcome_yao.count(4) == 1:	
			self.ninefunc = "遥克"
			self.haske(self.up_bottom_overcome_yao.index(4))
			return self.out_lines	
		if self.up_bottom_overcome_yao.count(4)>1:
			self.ninefunc = "遥克"
			stattr = self.bottom_attri[0]
			same_attr = [0]*4
			for index in range(4):
				if self.up_bottom_overcome_yao[index] == 4:
					if self.upper_attri[index] == stattr:
						same_attr[index] = 1		
			if same_attr.count(1) == 1:	
				self.haske(same_attr.index(1))				
				return self.out_lines	
		#弹射
		if self.up_bottom_overcome_yao.count(3)==1:
			self.ninefunc = "遥克"
			self.haske(self.up_bottom_overcome_yao.index(3))
			return self.out_lines		
		if self.up_bottom_overcome_yao.count(3)>1:
			self.ninefunc = "遥克"
			stattr = self.bottom_attri[0]
			same_attr = [0]*4
			for index in range(4):
				if self.up_bottom_overcome_yao[index] == 3:
					if self.upper_attri[index] == stattr:
						same_attr[index] = 1		
			if same_attr.count(1) == 1:	
				self.haske(same_attr.index(1))			
				return self.out_lines		
		if full_four == False:
			#别责
			if len(set(self.upperlist)) == 3:
				self.ninefunc = "别责"
				self.bieze()
				return self.out_lines
			#八专						
			if self.bottomlist[2] == today_stoeb:
				self.ninefunc = "八专"
				self.bazhuan()
				return self.out_lines	
			#反吟
			if self.upperlist[0] == self.eb_instance.opposited[self.eb_instance.names.index(today_stoeb)]:
				self.ninefunc = "反吟"
				self.fanyin()
				return self.out_lines	
		#昴星
		else:			
			self.angxing()
		return self.out_lines
	def out_res(self):
		print self.ninefunc
		print ' '.join(self.tri)
		#map(lambda x: self.skyplate_st[self.skyplate.index(x)]+x , self.tri)
		#tmpl = list(map(lambda x: self.skyplate_st[self.skyplate.index(x)]+x+"  "+ self.skygeneral[self.skyplate.index(x)], self.tri))
		tmpl = list(map(lambda x: self.skyplate_st[self.skyplate.index(x)]+x+"&nbsp&nbsp"+ self.skygeneral[self.skyplate.index(x)], self.tri))
		relation = ['']*3
		for index  in range(3):
			tmpattri = self.eb_instance.attribute[self.eb_instance.names.index(self.tri[index])]		
			if self.fe_instance.is_overcoming(self.bottom_attri[0], tmpattri) == True:
				relation[index] = '财'
			elif self.fe_instance.is_overcomed(self.bottom_attri[0], tmpattri) == True:
				relation[index] = '官'				
			elif self.fe_instance.is_child(self.bottom_attri[0], tmpattri) == True:
				relation[index] = '子'				
			elif self.fe_instance.is_parent(self.bottom_attri[0], tmpattri) == True:
				relation[index] = '父'				
			else:
				relation[index] = '比'

		tmpline = "<p>三传"
		tmpline = tmpline + "</p><p>"+relation[0]+"&nbsp&nbsp"+tmpl[0]
		tmpline = tmpline + "</p><p>"+relation[1]+"&nbsp&nbsp"+tmpl[1]
		tmpline = tmpline + "</p><p>"+relation[2]+"&nbsp&nbsp"+tmpl[2]
		tmpline = tmpline + "</p><p>详解</p><p>"
		file_name = sys.path[0]+"/liuren/output/"+self.bottomlist[0]+self.bottomlist[2]+"日干上"+self.upperlist[0]+".ini"
		print file_name
		f = None
		tmpstrss = ''
		try:
			f = open(file_name, "r")	
		except IOError:
			print "Error: open  %s file error!" % file_name
		else:  
			tmpstrss = f.read()
			tmpstrss = '<p>'+tmpstrss.replace('\n', '</p><p>')
			tmpline = tmpline+tmpstrss+"</p>"
		finally:
			if f :	
				f.close()
		self.out_lines = tmpline
		global_record_list.set_global_record(24, self.tri[0])
		global_record_list.set_global_record(28, self.tri[1])				
		global_record_list.set_global_record(32, self.tri[2])
		tmprelation = relation[0]	
		if tmprelation == '子':
			tmprelation = '食'	
		global_record_list.set_global_record(22, tmprelation)
		tmprelation = relation[1]	
		if tmprelation == '子':
			tmprelation = '食'
		global_record_list.set_global_record(26, tmprelation)				
		tmprelation = relation[2]	
		if tmprelation == '子':
			tmprelation = '食'
		global_record_list.set_global_record(30, tmprelation)
		global_record_list.set_global_record(25, self.skygeneral[self.skyplate.index(self.tri[0])])
		global_record_list.set_global_record(29, self.skygeneral[self.skyplate.index(self.tri[1])])				
		global_record_list.set_global_record(33, self.skygeneral[self.skyplate.index(self.tri[2])])

		global_record_list.set_global_record(23, self.skyplate_st[self.skyplate.index(self.tri[0])])
		global_record_list.set_global_record(27, self.skyplate_st[self.skyplate.index(self.tri[1])])				
		global_record_list.set_global_record(31, self.skyplate_st[self.skyplate.index(self.tri[2])])

	def haske(self, index):		
		self.tri[0] = self.upperlist[index]
		self.tri[1] = self.skyplate[self.eb_instance.names.index(self.tri[0])]
		self.tri[2] = self.skyplate[self.eb_instance.names.index(self.tri[1])]
		self.out_res()
	def angxing(self):
		stattr = self.st_instance.yinyang[self.st_instance.names.index(self.bottomlist[0])]
		#虎视转蓬
		if stattr == '阳':
			self.tri[0] = self.skyplate[9]
			self.tri[1] = self.upperlist[2]
			self.tri[2] = self.upperlist[0]
		#冬蛇掩目	
		else:	
			self.tri[0] = self.eb_instance.names[self.skyplate.index('酉')]
			self.tri[1] = self.upperlist[0]
			self.tri[2] = self.upperlist[2]			
		self.out_res()	
	def bieze(self):
		stattr = self.st_instance.yinyang[self.st_instance.names.index(self.bottomlist[0])]
		if stattr == '阳':
			st_coop = self.st_instance.cooperation[self.st_instance.names.index(self.bottomlist[0])]
			self.tri[0] = self.skyplate[self.skyplate_st.index(st_coop)]
		else:
			co_l = self.eb_instance.tricoop[self.eb_instance.names.index(self.bottomlist[2])]
			self.tri[0] = co_l[(co_l.index(self.bottomlist[2])+1)%3]
		self.tri[1] = self.upperlist[0]
		self.tri[2] = self.upperlist[0]			
		self.out_res()		
	def fuyin(self):
		stattr = self.st_instance.yinyang[self.st_instance.names.index(self.bottomlist[0])]	
		#不虞
		if self.up_bottom_overcome[0] != 0:
			self.tri[0] = self.upperlist[0]
		else:	
		#自任					
			if stattr == '阳':	
				self.tri[0] = self.upperlist[0]	
		#自信			
			else:
				self.tri[0] = self.upperlist[2]
		if self.tri[0] != self.eb_instance.xing[self.eb_instance.names.index(self.tri[0])]:
			self.tri[1] = self.eb_instance.xing[self.eb_instance.names.index(self.tri[0])] 	
		else:
			if stattr == '阳':	
				self.tri[1] = self.upperlist[2]		
			else:
				self.tri[1] = self.upperlist[0]	
				if self.tri[1] == self.tri[0]:
					self.tri[1] = self.upperlist[2]						
		if 	self.tri[1] != self.eb_instance.xing[self.eb_instance.names.index(self.tri[1])]:
			self.tri[2] = self.eb_instance.xing[self.eb_instance.names.index(self.tri[1])]
			if self.tri[2] == self.tri[0]:
				self.tri[2] = self.eb_instance.opposited[self.eb_instance.names.index(self.tri[1])]	
		else:
			self.tri[2] = self.eb_instance.opposited[self.eb_instance.names.index(self.tri[1])]	
		self.out_res()
	def fanyin(self):
		#无亲
		self.tri[0] = self.eb_instance.tricoop[self.eb_instance.names.index(self.upperlist[2])][0]
		self.tri[1] = self.upperlist[0]
		self.tri[2] = self.upperlist[2]			
		self.out_res()
	def bazhuan(self):
		stattr = self.st_instance.yinyang[self.st_instance.names.index(self.bottomlist[0])]	
		tmp_plate =   ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
		if stattr == '阳':
			self.tri[0] = tmp_plate[(tmp_plate.index(self.upperlist[0])+2)%12]
		else:
			self.tri[0] = tmp_plate[(tmp_plate.index(self.upperlist[3])-2+12)%12]
		self.tri[1] = self.upperlist[0]
		self.tri[2] = self.upperlist[0]			
		self.out_res()	
	def spec(self, spec_index):
		if spec_index == 1:
			self.tri[0] = '子'
			self.tri[1] = '未'
			self.tri[2] = '寅'
		if spec_index == 2:
			self.tri[0] = '巳'
			self.tri[1] = '亥'
			self.tri[2] = '巳'
		self.out_res()