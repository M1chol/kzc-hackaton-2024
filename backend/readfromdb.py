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
        self.date = str(datetime.datetime.now());
        self.experimentationDate = '';
        self.iconID = 0;
        self.like = 0;
    
    def UpdateParam(self, **kwargs):
        for paramName, newVal in kwargs.items():
            if str(paramName) != 'ID' and hasattr(self, paramName):
                setattr(self, paramName, newVal)
            else:
                raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{paramName}'")
class DBHandling():
    def __init__(self) -> None:
        self.db = TinyDB(DBLINK)
    
    def addEle(self, Element: Element) -> int:
        self.db.insert({'ID': self.__lastID()+1, 'x': Element.x, 'y': Element.y, 
                        'txt': Element.txt, 'authorID': Element.authorID,
                        'date': Element.date, 'iconID': Element.iconID, 
                        'experimentationDate': Element.experimentationDate,
                        'like': 0})
    
    def getAll(self) -> list:
        return self.db.all()
    
    # def likePost(self, ID:int):
    #     database = Query()
    #     like=self.db.search(database.ID == ID)[0]
    #     self.db.update({'like': like+1}, database.ID == ID)

    def __clearData(self) -> None:
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
    ele1.UpdateParam(x=130, y=15)
    DBHandler.addEle(ele1)
    # DBHandler.likePost(4)

    print(DBHandler.getAll())