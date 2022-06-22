
import functools
import hashlib

from flask import request

from app.models.token import Token


def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)
        acct = auth_user()  # custom account lookup function
        if acct==2:
            return func(*args, **kwargs)
        elif acct==1:
            return {'msg':'Su token es Incorrecto!!'},401
        elif acct==0:
            return {'msg':'Inicie sesion!!'},401
    return wrapper

def generate_hash(value:str):
    #lengh = 96 
    return hashlib.sha384(value.encode()).hexdigest()


def auth_user():
    token_str = request.headers.get('Authorization')
    if not token_str:
        return 0
    token = Token.get_by_token(token_str)
    if not token:
        return 1
    return 2
