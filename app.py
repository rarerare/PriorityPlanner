from flask import Flask;
import flask;
from flask import request;
import db_connector as dbms;
app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/', methods=['GET', 'POST'])
def render_main():
    return flask.render_template('rule.html', rules=get_rule())

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
def get_rule():
    return dbms.get_rule();