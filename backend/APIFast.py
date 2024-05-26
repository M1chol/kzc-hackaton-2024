from fastapi import FastAPI, HTTPException
from readfromdb import PostElement, POIElement, UPElement, DBPostHandling, DBPOIHandling, DBUPHandling, DBINFOHandling
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import datetime
import logging
# import CiastkowyPotwor


#TODO add user handling module

app = FastAPI()


origins = [
    "*",  # Allow all origins
    # or specify your origins:
    # "http://localhost:8080",
    # "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DBPostHandler = DBPostHandling()
DBPOIHandler = DBPOIHandling()
DBUPHandler = DBUPHandling()
DBINFOHandler = DBINFOHandling()

@app.get("/pins")
def allPOIs():
    return DBPOIHandler.getAll()

logging.basicConfig(level=logging.DEBUG)

@app.get("/fav/{UID}")
def get_favorites(UID: int):
    logging.debug(f"Received request for UID: {UID}")
    try:
        lista = DBUPHandler.getfavs(UID)
        logging.debug(f"getfavs returned: {lista}")
        
        if lista is None:
            raise HTTPException(status_code=404, detail="User not found or no favorites")

        nowa_lista = []
        for id in lista:
            post_name = DBPOIHandler.getPointName(id)
            logging.debug(f"getPointName for ID {id} returned: {post_name}")
            
            if post_name is None:
                raise HTTPException(status_code=404, detail=f"Post with ID {id} not found")
            
            nowa_lista.append({"POSTID": id, "PostName": post_name})

        logging.debug(f"Returning: {nowa_lista}")
        return nowa_lista
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/pin/{POIID}")
def allPOIs(POIID: int) -> str:
    return DBINFOHandler.getinfo(POIID)

@app.get("/posts/{POIID}")
def search(POIID: int):
    posts = DBPOIHandler.getPost(POIID)
    wszystkie_wyniki=[DBPostHandler.getEleByID(ID) for ID in posts if dict(DBPostHandler.getEleByID(ID))['experimentationDate'] > dict(DBPostHandler.getEleByID(ID))['date']]
    return wszystkie_wyniki

class UserInfo(BaseModel):
    UID: int

@app.post("/users/login")
def login(UserInfo):
    pass


class PostEle(BaseModel):
    pinID: int
    text: str
    authorID: str
    iconID: int

@app.post("/pins")
def addnewpost(post: PostEle):
    try:
        id = DBPostHandler.addEle(post)
        DBPOIHandler.addPost(post.pinID, id)
        return {'id': id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

