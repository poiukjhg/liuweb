# -*- coding: utf-8 -*- 
from run import run as run_func
from datetime import datetime, timedelta
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
	else:
		fortell_time = datetime.now()
		fortell_time_str = fortell_time.strftime('%Y-%m-%d %H:%M:%S')						
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
	run_func(fortell_time, fortell_zone, fortell_index)	
