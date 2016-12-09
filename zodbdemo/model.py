import persistent
import persistent.list
from datetime import datetime


class Talk(persistent.Persistent):

    def __init__(
        self,
        name='',
        title='',
        date_time=datetime.now(),
        topics=persistent.list.PersistentList()
    ):
        self.name = name
        self.title = title
        self.date_time = date_time
        self.topics = topics
