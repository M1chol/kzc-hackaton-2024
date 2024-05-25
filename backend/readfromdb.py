from tinydb import TinyDB, Query
import datetime

DBLINK = 'backend\db.json'

# db = TinyDB('db.json')
class Element():
    def __init__(self, authorID: str) -> None:
        self.ID = 0;
        self.x = 0;
        self.y = 0;
        self.txt = '';
        self.authorID = authorID;
        self.date = str(datetime.datetime(2000,1,1));
        self.iconID = 0;
    
    def UpdateParam(self, **kwargs):
        for paramName, newVal in kwargs.items():
            if hasattr(self, paramName):
                setattr(self, paramName, newVal)
            else:
                raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{paramName}'")
class DBHandling():
    def __init__(self) -> None:
        self.db = TinyDB(DBLINK)
    
    def addEle(self, Element: Element) -> int:
        self.db.insert({'ID': self.__lastID()+1, 'x': Element.x, 'y': Element.y, 
                        'txt': Element.txt, 'authorID': Element.authorID,
                        'date': Element.date, 'iconID': Element.iconID})
    
    def getAll(self) -> list:
        return self.db.all()
    
    def _clearData(self) -> None:
        self.db.truncate()
    
    def __lastID(self) -> int:
        last = 0;
        for ele in iter(DBHandler.db):
            if ele['ID'] > last:
                last = ele['ID']
        return last

if __name__ == '__main__':
    DBHandler = DBHandling()
    ele1 = Element("twoja stara")
    ele1.UpdateParam(ID = 4, x=130, y=15)
    DBHandler.addEle(ele1)

    print(DBHandler.getAll())