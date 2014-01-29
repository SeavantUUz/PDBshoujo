#coding:utf-8
import os,calendar
from datetime import datetime

class Node(object):
    def __init__(self,**kwargs):
        try:
            self.title     = kwargs['title']
            self.abstrct   = kwargs['abstrct']
            self.content   = kwargs['content']
            self.tags      = kwargs['tags']
            self.archive   = kwargs['archive']
            self.date      = kwargs['date']
            self.path      = kwargs['path']
        except KeyError:
            raise Exception('Ouch! Properties not enough!!\n')
        self.timestamp = min(self.utctimestamp(self.date),\
                         self.ctime(self.path,self.title))
            
    def utctimestamp(self,value):
        date = value.strip()
        d = datetime.strptime(date,'%Y-%m-%d:%H')
        return calendar.timegm(d.utctimetuple())

    def ctime(self,path,title):
        filename = os.path.join(path,title)
        return os.path.getctime(filename)

    @property
    def feed_date(self):
        date = datetime.datetime.fromtimestamp(self.timestamp)
        d = date.strftime('%Y-%m-%dT%H:%M:%S')
        return d+'+00:00'

    def __lt__(self,other):
        return self.timestamp > other.timestamp

    def __unicode__(self):
        return self.title

    def __str__(self):
        return unicode(self).encode('utf-8')
