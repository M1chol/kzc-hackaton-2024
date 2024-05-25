from fastapi import FastAPI
from readfromdb import PostElement, POIElement, UPElement, DBPostHandling, DBPOIHandling
#TODO add user handling module

app = FastAPI()

DBPOIHandler = DBPOIHandling()

@app.getPOIs("/")
def allPOIs():
    return DBPOIHandler.getAll()