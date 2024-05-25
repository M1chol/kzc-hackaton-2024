from fastapi import FastAPI
from readfromdb import PostElement, POIElement, UPElement, DBPostHandling, DBPOIHandling, DBUPHandling
from fastapi.middleware.cors import CORSMiddleware
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

@app.get("/posts")
def search(POIID: int):
    return DBPOIHandler.getPost(POIID)

@app.post("/pin")
def addnewpost(post: PostElement, pinID: int):
    id = DBPostHandler.addEle(post)
    DBPOIHandler.addPost(pinID, id)


# @app.post("/users/signup/{UID}")
# def createUser(UID):
#     DBUPHandler.addUser(UID)

# @app.post("/users/login/{UID}")
# def login(UID):
#     pass
