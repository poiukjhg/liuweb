# -*- coding: utf-8 -*- 
from gettodayse import todayse
import earthbranch
class get_yearloop:
	def __init__(self, gender = '男', birth = '1981', cur_year = '2017'):	
		self.eb_instance = earthbranch.earthbranch()	
		birth_eb = self.get_year(birth)
		year_diff = (int(cur_year) - int(birth))%12
		if gender == '男':
			index = (2+year_diff)%12
		else:
			index = (8+12-year_diff)%12

		self.res = "年命："+birth_eb+"  行年："+self.eb_instance.names[index]
	def return_res(self):
		return self.res
	def get_year(self, year):		
		yebtmpindex = int(year)
		yebtmpindex = (yebtmpindex-3)%12
		return self.eb_instance.names[yebtmpindex-1]	