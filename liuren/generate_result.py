# -*- coding: utf-8 -*- 
import fiveelements
import earthbranch
import skytrunk
import skygeneral
import trishift
import output_results
class generate_result():
	def __init__(self, today_st, today_eb, month_general, foretell_hour):
		'''
		print today_st
		print today_eb
		print month_general
		print foretell_hour
		'''
		self.skyplate =   ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
		self.skyplate_st = ['']*12
		self.skygeneral = ['贵','蛇','雀','合','勾','龙','空','虎','常','玄','阴','后']
		self.eb_instance = earthbranch.earthbranch()
		self.st_instance = skytrunk.skytrunk()
		self.fe_instance = fiveelements.fiveelements()
		self.sg_instance = skygeneral.skygeneral()
		self.trishift = None
		self.st = today_st
		self.eb = today_eb
		self.foretell_hour = foretell_hour
		self.month_general = month_general
		self.upper_four =  ['',       '', '',       '']
		self.bottom_four = [today_st, '', today_eb, '']
		self.trigeneral = ['']*3
		self.triline = ''
	def generate_skyplate(self):
		eloopindex = self.eb_instance.names.index(self.month_general)
		fortellindex = self.eb_instance.names.index(self.foretell_hour)
		tmpst = self.st_instance.names
		tmpst.append('&nbsp&nbsp&nbsp&nbsp')
		tmpst.append('&nbsp&nbsp&nbsp&nbsp')
		for index in range(12):	
			self.skyplate[(fortellindex+index)%12] = self.eb_instance.names[(index+eloopindex)%12]			
		for index in range(12):	
			self.skyplate_st[(self.skyplate.index(self.eb)+index)%12] = tmpst[(index+tmpst.index(self.st))%12]
		#for index in range(12):				
		#	print self.skyplate_st[index]+ self.skyplate[index]	
			
	def generate_four(self):
		st2eb = self.st_instance.stoeb[self.st_instance.names.index(self.st)]
		#print '天干转地支 '+ st2eb
		tmpstr = self.skyplate[self.eb_instance.names.index(st2eb)]
		#print '天干上 '+tmpstr
		self.upper_four[0] = tmpstr
		self.bottom_four[1] = tmpstr
		self.upper_four[1] = self.skyplate[self.eb_instance.names.index(tmpstr)]
		#print '天干阴神'+self.upper_four[1]
		tmpstr = self.skyplate[self.eb_instance.names.index(self.eb)]
		#print '地支上神'+tmpstr
		self.upper_four[2] = tmpstr
		self.bottom_four[3] = tmpstr
		self.upper_four[3] = self.skyplate[self.eb_instance.names.index(tmpstr)]
		#print '地支阴神'+self.upper_four[3]
	def generate_skygeneral(self):
		self.skygeneral = self.sg_instance.get_skygeneral_list(self.st, self.skyplate, self.foretell_hour)
	def generate_trishift(self):
		self.trishift = trishift.trishift(self.upper_four, self.bottom_four, self.skyplate, self.skygeneral, self.skyplate_st)
		'''
		trilist = self.trishift.build_trishift()
		self.trigeneral[0] = self.skygeneral[self.skyplate.index(trilist[0])]
		self.trigeneral[1] = self.skygeneral[self.skyplate.index(trilist[1])]
		self.trigeneral[2] = self.skygeneral[self.skyplate.index(trilist[2])]
		'''
		self.triline = self.trishift.build_trishift()
if __name__ == '__main__':
	'''
	gs = generate_result('癸','酉','子','辰')
	gs.generate_skyplate()
	gs.generate_four()
	gs.generate_skygeneral()
	print '天盘'
	print ' '.join(gs.skyplate)
	print '天将'	
	print ' '.join(gs.skygeneral)
	print '四课'
	print 'bottom'
	for index in range(4):
		print gs.bottom_four[3-index]
	print 'upper'
	for index in range(4):
		print gs.upper_four[3-index]
	output11 = output_results.output_results(gs.st, gs.eb, gs.month_general, gs.foretell_hour, gs.skyplate, gs.skygeneral, gs.bottom_four, gs.upper_four)
	output11.output()
	gs.generate_trishift()
'''

	for item in ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']:		
		#print "新一课占时"+item+"\n\r"
		gs = generate_result('癸','酉','子',item)
		gs.generate_skyplate()
		gs.generate_four()
		gs.generate_skygeneral()
		gs.generate_trishift()	
		output11 = output_results.output_results(gs.st, gs.eb, gs.month_general, gs.foretell_hour, gs.skyplate, gs.skygeneral, gs.bottom_four, gs.upper_four, gs.triline)
		output11.output()
				

