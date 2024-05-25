from tinydb import TinyDB, Query
import datetime

# db = TinyDB('db.json')
class Element():
    def __init__(self) -> None:
        self.ID = 0;
        self.x = 0;
        self.y = 0;
        self.txt = '';
        self.authorID = '';
        self.date = datetime(2000,1,1);
        self.iconID = 0;
class DBHandling():
    def __init__(self) -> None:
        self.db = TinyDB('db.json')
    
    def addEle(self, Element: Element) -> None:
        self.db.insert({'ID': Element.ID, 'x': Element.x, 'y': Element.y, 
                        'txt': Element.txt, 'authorID': Element.authorID,
                        'date': Element.date, 'iconID': Element.iconID})