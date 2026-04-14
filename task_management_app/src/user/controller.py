from src.user.dtos import UserSchema , LoginSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from  fastapi import HTTPException
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def register(body:UserSchema , db:Session):
    print(body)
    ##1-Username validations
    ##2-Email Validations
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(400 , detail="Username already exists..")
    
    is_user = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_user:
        raise HTTPException(400 , detail="Email already exists..")
    
    hash_password = get_password_hash(body.password)

    new_user = UserModel(
        name=body.name,
        username=body.username,
        hash_password=hash_password,
        email=body.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(body:LoginSchema , db:Session):
    print(body)
    return "Login Done"