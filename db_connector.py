import mysql.connector
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
