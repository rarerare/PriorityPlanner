from flask import Flask;
import flask;
from flask import request;
import db_connector as dbms;
from pq_planner import Task
import datetime
app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/', methods=['GET', 'POST'])
def render_main():
    return flask.render_template('index.html', rules=get_rule())

@app.route('/addRule', methods=['GET', 'POST'])
def add_rule():
    rule={'descrip': request.form['descrip'], 'exp_date': request.form['exp_date'], 'exp_hr': request.form['exp_hr']}
    dbms.add_rule(rule)
    return flask.render_template('rule.html', rules=get_rule())

@app.route('/logRead', methods=['GET', 'POST'])
def log_read():
    if float(request.form['minUsed'])==0:
        return flask.redirect('/readLog')
    readLog={'title':request.form['title'], 'pgs':request.form['pgs'], 'minUsed':request.form['minUsed']}
    dbms.log_read(readLog)
    return flask.redirect('/readlog')

@app.route('/readlog', methods=['GET', 'POST'])
def render_read_log():
    return flask.render_template('readLog.html', readLogs=dbms.get_log())
@app.route('/openBreach', methods=['GET', 'POST'])
def render_breach_detail():
    rule_id=request.args.get('id')
    return flask.render_template('breachRule.html', breach_detail=dbms.get_breach_detail(rule_id), rule_id=rule_id)

@app.route('/recordBreach', methods=['GET', 'POST'])
def record_breach():
    severity=request.form['severity']
    rule_id=request.form['rule_id']
    dbms.breach_rule({'rule_id':rule_id, 'severity': severity})
    return flask.render_template('breachRule.html', breach_detail=dbms.get_breach_detail(rule_id), rule_id=rule_id)
@app.route('/recordPerfect', methods=['GET', 'POST'])
def recordPerfect():
    dbms.recordPerfect()
    return flask.render_template('perfectDay.html',perfectDays=dbms.getPerfectDays())
@app.route('/showPerfectDay', methods=['GET', 'POST'])
def showPerfectDay():
    return flask.render_template('perfectDay.html', perfectDays=dbms.getPerfectDays())
def get_rule():
    return dbms.get_rule();

@app.route('/addTask', methods=['GET', 'POST'])
def addTask():
    due_date=request.form['due_date']
    if due_date!="none":
        due_dt_str=(datetime.datetime.strptime(due_date+" "+request.form['due_hr']+":"+request.form['due_min'], "%m/%d/%Y %H:%M")).strftime('%Y-%m-%d %H:%M:%S')
    else:
        due_dt_str=None
    task=Task( request.form['descrip'], due_dt_str, request.form['priority'], request.form['budget_hr'], 1)
    dbms.add_task(task)
    return flask.render_template('index.html', rules=get_rule())

@app.route('/renderAddTaskPage', methods=['GET', 'POST'])
def renderAddTaskPage():
    return flask.render_template('addTask.html')
