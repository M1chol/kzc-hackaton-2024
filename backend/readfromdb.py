from tinydb import TinyDB, Query
import datetime

DB_POSTS_LINK = r'backend\databases\posts.json'
DB_P_O_I_LINK = r'backend\databases\pointsofintrest.json'
DB_UP_LINK = r"backend\databases\userfav.json"
DB_INFO_LINK = r"backend\databases\info.json"
#https://www.youtube.com/watch?v=xYG89rB6c5k

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

    def getEleByID(self, ID: int) -> dict:
        listaslow = self.db.all()
        znaleziony_element = next((element for element in listaslow if element['ID'] == ID), None)
        return znaleziony_element

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
    
    def getPointName(self, PointID: int) -> str:
        database = Query()
        place = self.db.get(database.ID == PointID)
        if place is not None:
            posts = place.get('name', [])
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

#!ODZIELENIE USERPLACES OD INFO

class InfoElement(ElementType):
    def __init__(self) -> None:
        self.PINID = 0
        self.info = ''
        super().__init__()
class DBINFOHandling():
    def __init__(self) -> None:
        self.db = TinyDB(DB_INFO_LINK)

    def _addEle(self, Element: InfoElement) -> None:
        for ele in iter(self.db):
            if ele['PINID'] == Element.PINID:
                return
        self.db.insert({'PINID': Element.PINID, 'info': Element.info})

    def getinfo(self, PINID: int) -> str:
        listaslow = self.db.all()
        znaleziony_element = next((element for element in listaslow if element['PINID'] == PINID),  None)
        if znaleziony_element:
            return znaleziony_element['info']
        else:
            return 'PLS HELP ME IM STUCK IN INFO PANEL'

if __name__ == '__main__':
    DBPostHandler = DBPostHandling()
    DBPOIHandler = DBPOIHandling()
    DBUPHandler = DBUPHandling()
    DBINFOHandler = DBINFOHandling()
    # DBUPHandler.addUser(1)
    ele = InfoElement()
    ele.UpdateParam(PINID=12,  info='Można tu kupić napoje oraz zimne przekąski. WAT Connect poleca kanapki z kurczakiem')
    DBINFOHandler._addEle(ele)

    # DBPOIHandler.addPost(1,1)
    # print(DBPOIHandler.getPost(1))
    # print(dict(DBPostHandler.getEleByID(1)))

    # ele = InfoElement()
    # ele.UpdateParam(PINID = 1, info = "teiwuhgtyuewsgwye")
    # DBINFOHandler._addEle(ele)

    # print(DBINFOHandler.getinfo(3))
    # print(DBPostHandler.getEleByID(1))
    # lista = DBUPHandler.getfavs(1)
    # nowa_lista = [{"POSTID": id, "PostName": DBPOIHandler.getPointName(id)} for id in lista]
    # print(nowa_lista)


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