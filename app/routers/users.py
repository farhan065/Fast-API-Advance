
from .. import model , schemas, utils
from ..utils import hash_password
from ..database import engine, get_db
from fastapi import Depends, FastAPI, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List




router = APIRouter(
    prefix="/users",
    tags=['Users']
)








### Starting Creating routes for User Model

# ### Using SQLAlchemy ORM

### Creating User Account which will store email and password and which mean I am using POST method
@router.post("/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(new_user: schemas.UserCreate, db: Session = Depends(get_db)):
    # hash the password - new_user.password
    hashed_password = hash_password(new_user.password)
    #print(f"The hashed password is: {hashed_password}") # <-- ADD THIS LINE

    new_user.password = hashed_password
    user_model = model.UserModel(**new_user.dict())

    db.add(user_model)
    db.commit()
    db.refresh(user_model)

    return user_model


### Get a specific user by id
@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(model.UserModel).filter(model.UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} was not found")
    return  user
