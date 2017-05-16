from peewee import *
import datetime
import liuren_dbcfg
'''
database =  MySQLDatabase(
        database = 'liuq',
        host = 'localhost',
        port = 3306, 
        user = 'zz',
        passwd = '1234',
        charset = 'utf8'
        ) 
'''
class BaseModel(Model):
    class Meta:
        database = liuren_dbcfg.database

class liuq_log(BaseModel):
    _id = PrimaryKeyField()
    plate_date = CharField(101)
    plate_file = TextField()
    save_time = DateTimeField(default=datetime.datetime.now)

def init_db():
    #global database
    liuren_dbcfg.database.connect()
    print liuren_dbcfg.database.create_tables([liuq_log], safe=True)


def add_liuq_log(pdate, ptest):
    #print ptest
    liuq_log.create(plate_date=pdate, plate_file=ptest)

def build_summary_from_date(plate_date):
    return 111


def get_detail_from_date(qid):
    l = liuq_log.get(liuq_log._id==qid)
    print l.plate_file
    return l.plate_file

def get_liuq_all(qid=None): 
    if qid == None:
        l = liuq_log.select()
    else:
        l = liuq_log.select().where(liuq_log._id==qid)
    L = {}
    item = {}
    index = 0
    for i in l:
        item = {'id': i._id,'summary': build_summary_from_date(i.plate_date), 'detail': i.plate_file}
        L[index] = item
    return L

def del_liuq_(qid):
    try:
        n_ser = liuq_log.get(liuq_log._id==qid)
    except Exception, e:        
        return
    finally:
        n_ser.delete_instance()
    
def destroy_db():
    liuren_dbcfg.database.close()

if __name__ == '__main__':
    try:
        init_db()
        add_liuq_log('test', 'test')
        destroy_db()
    except Exception, e:
        print e
