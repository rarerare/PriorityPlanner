import datetime
import sched, time
from sched import scheduler
class Task:
    """A task"""
    def __init__(self, descrip, due_datetime, priority, budget_hr, user_id):
        self.descrip = descrip
        self.due_datetime=due_datetime
        self.priority=priority
        self.budget_hr=budget_hr
        
        self.create_date=datetime.datetime.now()
        self.user_id=user_id
        self.hr_left=budget_hr

    def to_json(self):
        return {'descrip':self.descrip, 'due_datetime': self.due_datetime, 'priority':self.priority\
        , 'budget_hr':self.budget_hr \
        ,'create_date':self.create_date.strftime('%Y-%m-%d %H:%M:%S'), 'user_id':self.user_id, 'hr_left':self.hr_left}


        
class Rule(object):
    """docstring for Rule"""
    def __init__(self, descrip):
        self.descrip=descrip
        self.breachCnt=0


        



        


        
        