from peewee import *
import datetime
database =  MySQLDatabase(
        database = 'liuq',
        host = 'localhost',
        port = 3306, 
        user = 'zz',
        passwd = '1234',
        charset = 'utf8'
        ) 

class BaseModel(Model):
    class Meta:
        database = database

class liuq_log(BaseModel):
    _id = PrimaryKeyField()
    plate_date = CharField(101)
    plate_file = TextField()
    save_time = DateTimeField(default=datetime.datetime.now)

def init_db():
    global database
    database.connect()
    print database.create_tables([liuq_log], safe=True)


def add_liuq_log(pdate, ptest):
    try:
        n_ser = liuq_log.get(liuq_log.plate_date==pdate)
    except Exception, e:        
        #print e 
        liuq_log.create(plate_date=pdate, plate_file=ptest)
    
def destroy_db():
    database.close()

if __name__ == '__main__':
    try:
        init_db()
        add_liuq_log('test', 'test')
        destroy_db()
    except Exception, e:
        print e
