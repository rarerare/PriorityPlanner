from flask import Flask;
import flask;
from flask import request;
import db_connector as dbms;
app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/', methods=['GET', 'POST'])
def render_main():
    return flask.render_template('index.html', rules=get_rule())

@app.route('/addRule', methods=['GET', 'POST'])
def add_rule():
    rule=request.form['descrip']
    dbms.add_rule(rule)
    return flask.render_template('index.html', rules=get_rule())


def get_rule():
    return dbms.get_rule();