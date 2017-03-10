# -*- coding: utf-8 -*- 
import earthbranch
import skytrunk
from xingli import SolarTerm as xingli
from datetime import datetime, timedelta
import math
class todayse:
	def __init__(self, curtime = datetime.now(), localzone = 8):
		self.eb_instance = earthbranch.earthbranch()
		self.st_instance = skytrunk.skytrunk()	
		#print curtime
		tmphour = curtime.strftime('%H')
		self._replace_time = curtime
		self.real_time = curtime
		if int(tmphour)>22:
			self._replace_time = curtime+timedelta(days=1, hours=-23)		
		self.nowtime = self._replace_time.strftime('%Y-%m-%d %H:%M:%S')			
		self.year = self.nowtime[0:4]
		self.month = self.nowtime[5:6]
		self.day = self.nowtime[8:9]
		self.hour = self.nowtime[11:]
		self.is_set_hour = False
		self.fortell_hour_index = 0
		xinlitmp = xingli()
		self.jieqi = xinlitmp.mytest(int(self.year))
		cday = curtime
		year_start = datetime.strptime(self.jieqi[0], '%Y-%m-%d %H:%M:%S') 		
		if cday < year_start:
			self.year = str(int(self.year)-1)
			self.jieqi = xinlitmp.mytest(int(self.year)	)
		#print self.nowtime	
		##to current time zone
		#北京是东八区
		for index in range(24):
			temptime = datetime.strptime(self.jieqi[index], '%Y-%m-%d %H:%M:%S')
			temptime = temptime+timedelta(hours=localzone)
			self.jieqi[index] = temptime.strftime('%Y-%m-%d %H:%M:%S')
		#print ' '.join(self.jieqi)
		#xinlitmp.paiYue(int(self.year))
		#xinlitmp.paiYue(int(self.year)-1)
		self.jieqi_index = 0
	def get_year(self):
		self.ystmpindex = int(self.year[-1])
		self.ystmpindex = self.ystmpindex -3
		if self.ystmpindex<0:
			self.ystmpindex = self.ystmpindex+10		
		self.yebtmpindex = int(self.year)
		self.yebtmpindex = (self.yebtmpindex-3)%12
		return self.st_instance.names[self.ystmpindex-1]+self.eb_instance.names[self.yebtmpindex-1]			
	def get_month(self):		
		lasttmptime = datetime.strptime(self.year+'-01-01 01:01:59', '%Y-%m-%d %H:%M:%S')
		nowtt = self.real_time
		for index in range(12):
			tmptime = datetime.strptime(self.jieqi[index*2], '%Y-%m-%d %H:%M:%S')
			#print lasttmptime.strftime('%Y-%m-%d %H:%M:%S')+" "+self.nowtime+" "+tmptime.strftime('%Y-%m-%d %H:%M:%S')
			if nowtt > lasttmptime and nowtt<tmptime:			
				break
			lasttmptime = tmptime
		
		self.mstmpindex = (self.ystmpindex*2+(index-1))%10	 
		self.mebtmpindex = (index+2)%12
		self.get_jieqi_index()
		return self.st_instance.names[self.mstmpindex]+self.eb_instance.names[self.mebtmpindex-1]	
	def get_month_general(self):		
		lasttmptime = datetime.strptime(self.year+'-01-01 01:01:59', '%Y-%m-%d %H:%M:%S')
		nowtt = self.real_time
		for index in range(12):
			tmptime = datetime.strptime(self.jieqi[index*2+1], '%Y-%m-%d %H:%M:%S')
			#print lasttmptime.strftime('%Y-%m-%d %H:%M:%S')+" "+self.nowtime+" "+tmptime.strftime('%Y-%m-%d %H:%M:%S')
			if nowtt > lasttmptime and nowtt<tmptime:			
				break
			lasttmptime = tmptime
		self.mebtmpindex = (index+2)%12
		return self.eb_instance.cooperation[self.mebtmpindex-1]		
	def get_day(self):
		'''
		g = 4C + [C/4] + 5y + [y/4] + [3*(M+1) / 5] + d - 3
		z = 8C + [C/4] + 5y + [y/4] + [3*(M+1) / 5] + d + 7 + i (奇数月i=0，偶数月i=6)
		z = g+4C+10+i
		其中C是世纪数减一，y是年份后两位，M是月份，d是日数。1月和2月按上一年的13月
		因此C和y也要按上一年的年份搜索来取值
		14月来算。g除以10的余数是天干，z除以12的余数是地支。
		'''
		i = 0
		temptime = self.real_time.strftime('%Y-%m-%d')	
		year = temptime[0:4]		
		M = int(temptime[5:7])
		d = int(temptime[8:10])
		if M ==1 or M ==2:
			year = str(int(year)-1)
			M=M+12
		C = int(year[0:2])
		y = int(year[2:])
		if int(M)%2 ==0:
			i=6
		#print str(C)+" "+str(y)+" "+str(M)+" "+str(d)+ " "+str(i)
		g = 4*C + math.floor(float(C)/4) + 5*y + math.floor(float(y)/4) + math.floor(3*(float(M)+1) / 5) + d - 3
		'''
		print str(4*C)
		print str(math.floor(float(C)/4))
		print str(5*y )
		print str(math.floor(float(y)/4))
		print str(math.floor(3*(float(M)+1) / 5))
		print str(d)
		'''
		#print str(g)
		stindex = int(g)%10-1
		z = g+4*C+10+i
		#print str(z)
		ebindex = int(z)%12-1
		self.debtmpindex = ebindex
		self.dsttmpindex = stindex
		return self.st_instance.names[stindex]+self.eb_instance.names[ebindex]	
	def get_fortell_hour(self):
		if self.is_set_hour == False:
			tmpindex = (int(self.hour.lstrip()[0:2])+1)/2
			self.fortell_hour_index = tmpindex
		return self.eb_instance.names[self.fortell_hour_index ]
	def get_hour(self):
		heb = self.get_fortell_hour()
		tmpstart = (self.dsttmpindex%5)*2
		#print str(tmpstart)
		self.hsttmpindex = (self.fortell_hour_index+tmpstart)%10
		return self.st_instance.names[self.hsttmpindex]+heb
	def set_fortell_hour(self, index):
		self.fortell_hour_index = index
		self.is_set_hour = True
	def get_jieqi_index(self):
		lasttmptime = datetime.strptime(self.year+'-01-01 01:01:59', '%Y-%m-%d %H:%M:%S')
		nowtt = self.real_time
		for index in range(24):
			tmptime = datetime.strptime(self.jieqi[index], '%Y-%m-%d %H:%M:%S')
			#print lasttmptime.strftime('%Y-%m-%d %H:%M:%S')+" "+self.nowtime+" "+tmptime.strftime('%Y-%m-%d %H:%M:%S')
			if nowtt > lasttmptime and nowtt<tmptime:			
				break
			lasttmptime = tmptime		
		self.jieqi_index = index
	def get_front_jieqi(self):
		jqB = [ #节气表  
        "立春","雨水","惊蛰","春分","清明","谷雨","立夏","小满","芒种","夏至","小暑","大暑","立秋","处暑","白露",  
        "秋分","寒露","霜降","立冬","小雪","大雪","冬至","小寒","大寒"];  		
		return jqB[self.jieqi_index-1]+":"+self.jieqi[self.jieqi_index-1]	
	def get_after_jieqi(self):
		jqB = [ #节气表  
        "立春","雨水","惊蛰","春分","清明","谷雨","立夏","小满","芒种","夏至","小暑","大暑","立秋","处暑","白露",  
        "秋分","寒露","霜降","立冬","小雪","大雪","冬至","小寒","大寒"]; 		
		return jqB[self.jieqi_index]+":"+self.jieqi[self.jieqi_index]	

if __name__ == "__main__":
	
	test = todayse()	
	print  test.real_time
	print "年"+test.get_year()+" 月"+test.get_month()+" 日"+test.get_day() + " 月将"+test.get_month_general()+ " 占时"+test.get_hour()+" 节气"+test.get_front_jieqi()+" "+test.get_after_jieqi()
	print '2009-07-16 12:59:59'
	test = todayse(datetime.strptime('2009-07-16 12:59:59', '%Y-%m-%d %H:%M:%S'))
	print "年"+test.get_year()+" 月"+test.get_month()+" 日"+test.get_day() + " 月将"+test.get_month_general()+ " 占时"+test.get_hour()+" 节气"+test.get_front_jieqi()+" "+test.get_after_jieqi()
	print '2016-11-06 23:19:59' 
	test = todayse(datetime.strptime('2016-11-06 23:19:59', '%Y-%m-%d %H:%M:%S'))
	print "年"+test.get_year()+" 月"+test.get_month() +" 日"+test.get_day()+ " 月将"+test.get_month_general()+ " 占时"+test.get_hour()+" 节气"+test.get_front_jieqi()+" "+test.get_after_jieqi()

	print '2016-11-06 23:59:59'
	test = todayse(datetime.strptime('2016-11-06 23:59:59', '%Y-%m-%d %H:%M:%S'))
	test.set_fortell_hour(4)
	print "年"+test.get_year()+" 月"+test.get_month()+" 日"+test.get_day() + " 月将"+test.get_month_general()+ " 占时"+test.get_hour()+" 节气"+test.get_front_jieqi()+" "+test.get_after_jieqi()

    


