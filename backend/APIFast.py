from fastapi import FastAPI
from readfromdb import PostElement, POIElement, UPElement, DBPostHandling, DBPOIHandling
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

DBPOIHandler = DBPOIHandling()

@app.get("/pins")
def allPOIs():
    return DBPOIHandler.getAll()

@app.get("/posts/{POIID}")
def search(POIID):
    return DBPOIHandler.getPost(POIID)