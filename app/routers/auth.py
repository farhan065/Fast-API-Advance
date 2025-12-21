from fastapi import Depends, FastAPI, Response, status, HTTPException, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List

from  .. import model , schemas, utils, oauth2

from ..database import get_db # alternate way  amra aivabe korte pari jodi app ta package hisabe na thake tahole FastApi_Advance_Course.app.database theke import korte hobe

router = APIRouter(

    tags=['Authentication']
)


### Here will go the authentication routes like login, signup, token generation etc.
@router.post("/login", response_model=schemas.TokenResponse)

##### Without OAuth2PasswordRequestForm
# def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):

#     user = db.query(model.UserModel).filter(model.UserModel.email == user_credentials.email).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials user not found")
    
#     if not utils.verify_password(user_credentials.password, user.password):
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials wrong password")
    
#     # create a token
#     access_token = oauth2.create_access_token(data={"user_id": user.id})
#     # return token
    
#     return {"access_token": access_token, "token_type": "bearer"}

### Using OAuth2PasswordRequestForm (Faltu eikhane amra UserLogin schema use korchi na karon OAuth2PasswordRequestForm already ekta schema provide kore jeita form data hisabe username and password ney)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(model.UserModel).filter(model.UserModel.email == user_credentials.username).first()

    # If the user doesn't exist or the password is not valid, raise the same generic error.
    if not user or not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Credentials")

    # create a token
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    # return token
    
    return {"access_token": access_token, "token_type": "bearer"}

    

    