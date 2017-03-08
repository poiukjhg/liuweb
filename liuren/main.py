# -*- coding: utf-8 -*- 
from generate_result import generate_result
from output_results import output_results
from datetime import datetime, timedelta
from earthbranch import earthbranch
from gettodayse import todayse
import sys
if __name__ == '__main__':
	fortell_time = None
	fortell_index = None
	fortell_zone = None
	print "请输入时区, 默认为北京时区"	
	fortell_zone_str = raw_input()
	if len(fortell_zone_str) != 0:
		try:
			fortell_zone = int(fortell_zone_str)
		except :
			print "Error: %s 错误的时间形式!" % fortell_zone_str
			s=sys.exc_info()
			print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno)			
			sys.exit(0)
	print "请输入起课时间，形式为“1970-01-01 12:01:01”，默认为当前时"
	fortell_time_str = raw_input()
	if len(fortell_time_str) != 0:
		try:
			fortell_time = datetime.strptime(fortell_time_str, '%Y-%m-%d %H:%M:%S')	
		except :
			print "Error: %s 错误的时间形式!" % fortell_time_str
			s=sys.exc_info()
			print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno)
			sys.exit(0)			
	print "请输入占时，如 子或丑等, 默认为当前时"	
	fortell_hour_str = raw_input()
	if len(fortell_hour_str) != 0:
		try:
			fortell_index = earthbranch().names.index(fortell_hour_str)
			s=sys.exc_info()
			print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno)			
			sys.exit(0)
		except :
			print "Error: %s 错误的占时!" % fortell_hour_str
	if fortell_zone == None:
		fortell_zone = 8
	if fortell_time == None:	
		fortell_time = datetime.now()
		fortell_time_str = fortell_time.strftime('%Y-%m-%d %H:%M:%S')			
	gt = todayse(fortell_time, fortell_zone)

	if fortell_index != None:
		gt.set_fortell_hour(fortell_index)
	tmptoday = gt.get_day()
	tmptodayst = tmptoday[0:3]
	tmptodayeb = tmptoday[3:]
	tmphour = gt.get_hour()
	tmphoureb = tmphour[3:]
	tmpgeneral = gt.get_month_general()
	'''
	print "tmptoday "+tmptoday
	print "tmptodayst "+tmptodayst
	print "tmptodayeb "+tmptodayeb
	print "tmphour"+tmphour
	print "tmphoureb "+tmphoureb	
	'''
	print "起课时间："+	fortell_time_str
	print "占时: "+gt.get_year()+"年 "+gt.get_month()+"月 "+tmptoday+"日 "+tmphour+ "时 " + " 月将"+ tmpgeneral
	
	gs = generate_result(tmptodayst,tmptodayeb,tmpgeneral,tmphoureb)
	gs.generate_skyplate()
	gs.generate_four()
	gs.generate_skygeneral()
	gs.generate_trishift()	
	output11 = output_results(gs.st, gs.eb, gs.month_general, gs.foretell_hour, gs.skyplate, gs.skygeneral, gs.bottom_four, gs.upper_four, gs.triline)
	output11.output()	

