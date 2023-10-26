from jose import JWTError,jwt
from datetime import datetime,timedelta
#secret key
#algo

#expiration time

SECRET_KEY = "09wejd48jdj0284mdfh58f884493j"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def created_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt
