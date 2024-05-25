from tinydb import TinyDB, Query
import datetime

# db = TinyDB('db.json')
class Element():
    def __init__(self) -> None:
        self.x = 0;
        self.y = 0;
        self.txt = '';
        self.authorID = '';
        self.date = datetime(2000,1,1);
class DBHandling():
    def __init__(self) -> None:
        self.db = TinyDB('db.json')
    
    def addEle(self, Element) -> None:
        pass