from fastapi import FastAPI, HTTPException, Depends, status
from readfromdb import DBPostHandling, DBPOIHandling, DBUPHandling, DBINFOHandling, PostElement
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from typing import Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
import datetime

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
    try:
        info = DBINFOHandler.getinfo(POIID)
        return info
    except KeyError:
        raise HTTPException(status_code=404, detail="Nie znaleziono informacji dla podanego POIID")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/posts/{POIID}")
def search(POIID: int):
    try:
        posts = DBPOIHandler.getPost(POIID)
        wszystkie_wyniki=[DBPostHandler.getEleByID(ID) for ID in posts if dict(DBPostHandler.getEleByID(ID))['experimentationDate'] > dict(DBPostHandler.getEleByID(ID))['date']]
        return wszystkie_wyniki
    except KeyError:
        raise HTTPException(status_code=500, detail="Błąd przetwarzania danych - brak klucza w słowniku")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class UserInfo(BaseModel):
    UID: int

class PostEle(BaseModel):
    pinID: int
    txt: str
    authorID: str
    iconID: int

@app.post("/addnewpost")
def addnewpost(post: PostEle):
    try:
        npost = PostElement(post.authorID)
        npost.UpdateParam(txt = post.txt, iconID = post.iconID)
        id = DBPostHandler.addEle(npost)
        DBPOIHandler.addPost(post.pinID, id)
        return {'id': id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))






SECRET_KEY = "secretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    hashed_password: str
    UID: int  # Dodajemy pole UID

fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash("admin"),
        "UID": 1
    },
    "user": {
        "username": "user",
        "hashed_password": pwd_context.hash("user"),
        "UID": 2
    }
}

class UserInDB(User):
    hashed_password: str

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "UID": user.UID}, expires_delta=access_token_expires  # Dodajemy UID do danych w tokenie
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        UID: int = payload.get("UID")  # Pobieramy UID z tokena
        if username is None or UID is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=username)
    if user is None or user.UID != UID:
        raise credentials_exception

    # Dodajemy kod do obsługi żądania pobierającego ulubione elementy użytkownika
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

    return user