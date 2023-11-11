from jose import JWTError,jwt
from datetime import datetime,timedelta
from . import schemas
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
#secret key
#algo
outh2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#expiration time

SECRET_KEY = "09wejd48jdj0284mdfh58f884493j"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def created_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token:str,credential_exception):
    try:
        payload  = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id:str= payload.get("user_id")
        
        if id is None:
            raise credential_exception
        token_data = schemas.TokenData(id = id)
    except JWTError:
        raise credential_exception
    return token_data

def get_current_user(token:str = Depends(outh2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate",headers={"WWW-Authenticate":"Bearer"})
    return verify_access_token(token,credential_exception)
