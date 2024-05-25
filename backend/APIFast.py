from fastapi import FastAPI
from readfromdb import PostElement, POIElement, UPElement, DBPostHandling, DBPOIHandling
#TODO add user handling module

app = FastAPI()

DBPOIHandler = DBPOIHandling()

@app.get("/pins")
def allPOIs():
    return DBPOIHandler.getAll()

@app.get("/posts/{POIID}")
def search(POIID):
    return DBPOIHandler.getPost(POIID)