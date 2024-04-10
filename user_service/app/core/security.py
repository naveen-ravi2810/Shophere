from uuid import UUID
from datetime import datetime, timedelta
from fastapi import Cookie, Depends, HTTPException, status, Request, Response
from typing import Annotated
import bcrypt
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
import pytz
from app.core.settings import jwt_config

ist_tz = pytz.timezone('Asia/Kolkata')

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_hash_password(password: str, user_password: str) -> bool:
    return bcrypt.checkpw(password.encode(), user_password.encode())


def create_access_token(identity:UUID, payload:dict) -> str:
    curr_time = datetime.now(ist_tz)
    exp_time = curr_time + timedelta(seconds=jwt_config.JWT_ACCESS_EXPIRE_TIME_IN_SEC)
    payload.update({'iat':curr_time, 'exp':exp_time, 'sub':str(identity)})
    return jwt.encode(payload=payload, key=jwt_config.JWT_SECRET_KEY, algorithm='HS256')

def create_refresh_token(identity: UUID, payload:dict):
    curr_time = datetime.now(ist_tz)
    exp_time = curr_time + timedelta(seconds=jwt_config.JWT_REFRESH_EXPIRE_TIME_IN_SEC)
    payload.update({'fresh':True, 'iat':curr_time, 'exp':exp_time, 'sub':str(identity)})
    return jwt.encode(payload=payload, key=jwt_config.JWT_SECRET_KEY, algorithm='HS256')

def decode_token(token:str)->dict:
    data = jwt.decode(token, key=jwt_config.JWT_SECRET_KEY, algorithms='HS256')
    if 'fresh' in data:
        raise ValueError("Not a access token")
    return data



def get_curr_user(request: Request) -> str:
    try:
        access_token = request.cookies.get("access_token")
        if access_token == None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="no access token")
        else:
            return decode_token(access_token)
    except ExpiredSignatureError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Token expired")
    except InvalidSignatureError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid signature")
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
        