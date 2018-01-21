import datetime
import sched, time
from sched import scheduler
class Task:
    """A task"""
    def __init__(self, name, due_date, priority, est, user_id):
        self.name = name
        self.due_date=due_date
        self.priority=priority
        self.estimate_sec=est
        self.done=0
        self.create_date=datetime.datetime.now()
        self.user_id=user_id

    def to_json(self):
        return {'name':self.name, 'due_date': self.due_date, 'priority':self.priority\
        , 'estimate_sec':self.estimate_sec, 'done':self.done \
        ,'create_date':self.create_date.strftime('%Y-%m-%d %H:%M:%S'), 'user_id':self.user_id}


        
        