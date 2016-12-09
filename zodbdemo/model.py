import persistent
from datetime import datetime


class Talk(persistent.Persistent):

    def __init__(self):
        self.name = ''
        self.date = datetime.today()
        self.length = 0
        self.topics = []
