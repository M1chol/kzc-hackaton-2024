from tinydb import TinyDB, Query
import datetime

DB_POSTS_LINK = r'backend\databases\posts.json'
DB_P_O_I_LINK = r'backend\databases\pointsofintrest.json'
DB_UP_LINK = r"backend\databases\userfav.json"

#TODO Error handling
class ElementType():
    def __init__(self) -> None:
        pass
    def UpdateParam(self, **kwargs):
        for paramName, newVal in kwargs.items():
            if str(paramName) != 'ID' and hasattr(self, paramName):
                setattr(self, paramName, newVal)
            else:
                raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{paramName}'")


class PostElement(ElementType):
    def __init__(self, authorID: str) -> None:
        self.ID = 0
        self.txt = ''
        self.authorID = authorID;
        self.date = str(datetime.datetime.now())
        self.experimentationDate = str(datetime.datetime.now())
        self.iconID = 0
        self.like = 0
        super().__init__()
    
class DBPostHandling():
    def __init__(self) -> None:
        self.db = TinyDB(DB_POSTS_LINK)
    
    def addEle(self, Element: PostElement) -> int:
        lastID = self.__lastID()
        self.db.insert({'ID': lastID+1, 'txt': Element.txt, 'authorID': Element.authorID,
                        'date': Element.date, 'iconID': Element.iconID, 
                        'experimentationDate': Element.experimentationDate,
                        'like': 0})
        return lastID+1
    
    def getAll(self) -> list:
        return self.db.all()

    def __clearData(self) -> None:
        self.db.truncate()
    
    def __lastID(self) -> int:
        last = 0;
        for ele in iter(self.db):
            if ele['ID'] > last:
                last = ele['ID']
        return last

#!ODZIELANIE POI OD POST
class POIElement(ElementType):
    def __init__(self) -> None:
        self.ID = 0
        self.x = float
        self.y = float
        self.name = ''
        self.iconID = 0
        self.posts = []
        super().__init__()
class DBPOIHandling():
    def __init__(self) -> None:
        self.db = TinyDB(DB_P_O_I_LINK)

    def _addEle(self, Element: POIElement) -> int:
        lastID = self.__lastID()
        self.db.insert({'ID': lastID+1, 'x': Element.x, 'y': Element.y, 
                        'name': Element.name, 'iconID': Element.iconID, 'posts': []})
        return lastID

    def addPost(self, PlaceID: int , PostID: int):
        database = Query()
        place = self.db.get(database.ID == PlaceID)
        if place is not None:
            posts = place.get('posts', [])
            posts.append(PostID)
            self.db.update({'posts': posts}, database.ID == PlaceID)
        else:
            # Obsłuż sytuację, gdy PlaceID nie istnieje w bazie danych
            print("PlaceID not found in database.")

    def __lastID(self) -> int:
        last = 0;
        for ele in iter(self.db):
            if ele['ID'] > last:
                last = ele['ID']
        return last

    def getAll(self) -> list:
        return self.db.all()

    def getPost(self, PlaceID: int) -> list:
        database = Query()
        place = self.db.get(database.ID == PlaceID)
        if place is not None:
            posts = place.get('posts', [])
            return posts
        else:
            return [0]
        
#!ODZIELENIE POI OD USERPlACES
class UPElement(ElementType):
    def __init__(self, authorID: str) -> None:
        self.UID = 0
        self.favid = 12
        super().__init__()

class DBUPHandling():
    def __init__(self) -> None:
        self.db = TinyDB(DB_UP_LINK)

    def addUser(self, UID: int) -> None:
        User = Query()
        result = self.db.search(User.UID == UID)

        if not result:
            self.db.insert({'UID': UID, 'fav': []})
    
    def addEle(self, Element: UPElement) -> None:
        database = Query()
        userelement = self.db.get(database.UID == Element.UID)
        if userelement is not None:
            posts = userelement.get('fav', [])
            posts.append(Element.favid)
            self.db.update({'fav': posts}, database.UID == Element.UID)
        else:
            print("User not found in database.")

    def delEle(self, Element: UPElement) -> None:
        database = Query()
        userelement = self.db.get(database.UID == Element.UID)
        if userelement is not None:
            posts = userelement.get('fav', [])
            posts.remove(Element.favid)
            self.db.update({'fav': posts}, database.UID == Element.UID)
        else:
            print("User not found in database.")

    def getfavs(self, UID: int) -> list:
        database = Query()
        userelement = self.db.get(database.UID == UID)
        if userelement is not None:
            posts = userelement.get('fav', [])
            return posts
        else:
            print("User not found in database.")

    def getAll(self) -> list:
        return self.db.all()


if __name__ == '__main__':
    DBPostHandler = DBPostHandling()
    DBPOIHandler = DBPOIHandling()
    DBUPHandler = DBUPHandling()
    
    # DBUPHandler.addUser(1)
    ele = POIElement()
    ele.UpdateParam(x=12, y=532, name='gehuhgeuguehg')
    DBPOIHandler._addEle(ele)

    # ele2 = POIElement()
    # ele2.ID = ele2.UpdateParam(x=13, y=14, name='Hinczyk')
    # DBPOIHandler._addEle(ele2)
    # ele2.ID = ele2.UpdateParam(x=50, y=321, name='Tajne okopy drużyny 25')
    # DBPOIHandler._addEle(ele2)
    # ele2.ID = ele2.UpdateParam(x=2131250, y=5621, name='Składowisko portek Rektora')
    # DBPOIHandler._addEle(ele2)
    # ele2.ID = ele2.UpdateParam(x=10, y=31, name='Winda skrzydło któreś tam')

    # DBPOIHandler.addPost(3, 1)


    # print(DBUPHandler.getAll())