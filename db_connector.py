import mysql.connector
import datetime
DB_NAME='pq_planner'
TASK_TBL_NAME='task'
TASK_COLS='(name, due_date, done, estimate_sec, user_id, priority, create_date)'
TASK_VALS='(%(name)s, %(due_date)s, %(done)s, %(estimate_sec)s, %(user_id)s, %(priority)s, %(create_date)s)'
def add_task(task):
    cnx = mysql.connector.connect(user='root', password='drwssp',host='localhost',database=DB_NAME)
    addVisit=("INSERT INTO "+TASK_TBL_NAME+" "+TASK_COLS+ "VALUES"+TASK_VALS)
    cur=cnx.cursor()
    cur.execute(addVisit,task.to_json())
    cnx.commit()
    cnx.close()
def add_user(email, password):
    cnx = mysql.connector.connect(user='root', password='drwssp',host='localhost',database=DB_NAME)
    addUser=("INSERT INTO user(email, password) VALUES(%s,%s)")
    cur=cnx.cursor()
    cur.execute(addUser, (email,password))
    cnx.commit()
    cnx.close()

def add_rule(rule):
    cnx = mysql.connector.connect(user='root', password='drwssp',host='localhost',database=DB_NAME)
    addRule=("INSERT INTO rule (descrip, create_date, expire_time) VALUES(%s, %s, %s)")
    cur=cnx.cursor()
    exp_t_str=(datetime.datetime.strptime(rule['exp_date']+" "+rule['exp_hr'], "%m/%d/%Y %H")).strftime('%Y-%m-%d %H:%M:%S')
    rule_data=(rule['descrip'],datetime.datetime.now().strftime('%Y-%m-%d'), exp_t_str)
    cur.execute(addRule, rule_data)
    cnx.commit()
    cnx.close()

def get_rule():
    cnx = mysql.connector.connect(user='root', password='drwssp',host='localhost',database=DB_NAME)
    cur=cnx.cursor()
    query="SELECT id, descrip, breach_cnt, create_date, expire_time FROM rule"
    cur.execute(query)
    rules=[]
    for(id, descrip, breach_cnt, create_date, expire_time) in cur:
        rules.append({'id':id, 'descrip': descrip, 'breach_cnt':breach_cnt, 'create_date':create_date, 'exp_time': expire_time})
    cnx.close()
    return rules

def log_read(log):
    cnx = mysql.connector.connect(user='root', password='drwssp',host='localhost',database=DB_NAME)
    cur=cnx.cursor()
    addLog="INSERT INTO read_log(title, pg_num, time_min, date) VALUES(%s, %s, %s, %s)"
    logData=(log['title'],log['pgs'], log['minUsed'],datetime.datetime.now().strftime('%Y-%m-%d') )
    cur.execute(addLog, logData)
    cnx.commit()
    cnx.close()

def get_log():
    cnx = mysql.connector.connect(user='root', password='drwssp',host='localhost',database=DB_NAME)
    cur=cnx.cursor()
    query="SELECT title, pg_num, time_min, date FROM read_log"
    cur.execute(query)
    logs=[]
    for (title, pg_num, time_min, date) in cur:
        logs.append({'title':title, 'pg_num':pg_num, 'time_min': time_min, 'date':date})
    cnx.close()
    return logs

