from fastapi import FastAPI, HTTPException
from readfromdb import PostElement, POIElement, UPElement, DBPostHandling, DBPOIHandling, DBUPHandling
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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

@app.get("/pins")
def allPOIs():
    return DBPOIHandler.getAll()

@app.get("/posts/{POIID}")
def search(POIID):
    return DBPOIHandler.getPost(POIID)

class PostEle(BaseModel):
    pinID: int
    text: str
    authorID: str
    iconID: int

@app.post("/pin")
def addnewpost(post: PostEle):
    try:
        id = DBPostHandler.addEle(post)
        DBPOIHandler.addPost(post.pinID, id)
        return {'id': id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @app.post("/users/signup/{UID}")
# def createUser(UID):
#     DBUPHandler.addUser(UID)

# @app.post("/users/login/{UID}")
# def login(UID):
#     pass
