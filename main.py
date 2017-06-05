from flask import Flask,url_for,render_template, make_response,request, redirect
from liuren import run, liuren_db, global_record_list
from datetime import datetime, timedelta
import re

app = Flask(__name__)

@app.route('/')
def main_func():
	return "hello world"

@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name = None):
    #return 'Hello World!'
    return render_template('hello.html', name=name)

@app.route('/main/<username>', methods=['GET', 'POST'])
def main_page(username):
    return 'Main page %s!' %username

@app.route('/liu/<fortell00>')
def liu_page(fortell00):
	gender = fortell00[0:1]
	birth = fortell00[2:5]
	fortell = fortell00[5:]
	if len(fortell)>17 or len(fortell)<16 or int(fortell) == False:
		error = "error url(%s)" % (fortell or ' ')
		return render_template('error.html', error=error)
	fortell_time = fortell[0:4]+"-"+fortell[4:6]+"-"+fortell[6:8]+" "+fortell[8:10]+":"+fortell[10:12]+":"+fortell[12:14]
	fortell_zone = fortell[14:15]
	fortell_index = fortell[15:]	
	result = run.run(fortell_time, fortell_zone, fortell_index)
	resp = make_response(render_template('liu.html', res = result))
	resp.set_cookie('cur_fortel', fortell)
	tmpstr = global_record_list.get_global_record()
	resp.set_cookie('save_data', tmpstr)
	print 'save str '+ tmpstr	
	return resp

@app.route('/liuq/')
def liu_req():
	global_record_list.init_global_record()
	return render_template('liuq.html')

@app.route('/liuq/liu2/')
def liu_page2():
	fortell = request.args.get('fortell', '')
	gender = fortell[0:1]
	birth = fortell[1:5]
	fortell = fortell[5:]	
	if len(fortell)>17 or len(fortell)<16 or int(fortell) == False:
		error = "error url(%d)" % len(fortell)
		return render_template('error.html', error=error)
	fortell_time = fortell[0:4]+"-"+fortell[4:6]+"-"+fortell[6:8]+" "+fortell[8:10]+":"+fortell[10:12]+":"+fortell[12:14]
	fortell_zone = fortell[14:15]
	fortell_index = fortell[15:]	
	result = run.run(fortell_time, fortell_zone, fortell_index, gender, birth)
	if len(result) == 0:
		error = "no answer"
		return render_template('error.html', error=error)
	resp = make_response(render_template('liu.html', res = result))
	resp.set_cookie('cur_fortel', fortell_time)
        tmpstr = global_record_list.get_global_record()
        resp.set_cookie('save_data', tmpstr)
        print 'save str '+ tmpstr
	return resp

@app.route('/liu2/upload', methods=['POST'])
def upload_file():
	if request.method == 'POST':
		fstr = request.form['resstr']
		fstr_name = request.form['filename']
		liuren_db.init_db()
	#tmpstr = global_record_list.get_global_record()
		tmpstr = request.cookies.get('save_data')
		print 'save str '+ tmpstr
		tmpfortell = request.cookies.get('cur_fortel')
		liuren_db.add_liuq_log(tmpstr, fstr, tmpfortell)
		liuren_db.destroy_db()
    	'''
    	fstr = fstr.replace('</p>', '\n\r')
    	fstr = fstr.replace('<p>', '')
    	fstr = fstr.replace('&nbsp', ' ')
    	fstr = re.sub(r'<[^>]+>', "", fstr)
    	f = open('/tmp/'+fstr_name+'.html', 'w')
    	f.write(fstr)
    	f.close()
    	'''
    	return redirect('/liuq/')
@app.route('/liuql/')
def query_plate():
	liuren_db.init_db()
	tmp_str = liuren_db.get_liuq_all()
	liuren_db.destroy_db()
	print tmp_str
	return render_template('liuql.html', plate=tmp_str)

@app.route('/liuql/<plate_id>')
def query_plate_detail(plate_id):
	liuren_db.init_db()
	tmp_str = liuren_db.get_detail_from_date(plate_id)
	liuren_db.destroy_db()
	return tmp_str

@app.route('/delplate', methods=['POST'])
def delete_plate():
	if request.method == 'POST':
		plate_id = request.form['plate']
		liuren_db.init_db()
		tmp_str = liuren_db.del_liuq_(plate_id)
		liuren_db.destroy_db()	
	return 'ok', 200   

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
