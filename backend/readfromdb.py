from tinydb import TinyDB, Query
import datetime

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
        self.db = TinyDB('/backend/db.json')
    
    def addEle(self, Element: Element) -> None:
        self.db.insert({'ID': Element.ID, 'x': Element.x, 'y': Element.y, 
                        'txt': Element.txt, 'authorID': Element.authorID,
                        'date': Element.date, 'iconID': Element.iconID})
    
    def getAll(self) -> list:
        return self.db.all()

if __name__ == '__main__':
    DBHandler = DBHandling()
    ele1 = Element("twoja stara")
    ele1.UpdateParam(ID = 1, x=120, y=15)
    DBHandler.addEle(ele1)
    print(DBHandler.getAll())