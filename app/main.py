from fastapi import Depends, FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from random import randrange




import psycopg
from psycopg.rows import dict_row

from sqlalchemy.orm import Session





from . import model , schemas, utils
from .utils import hash_password
from .database import engine, get_db
from .routers import posts, users, auth, votes

### This is not needed as we are using alembic for migrations but it doesent harm to keep it here
#model.Base.metadata.create_all(bind=engine)


# session = SessionLocal()




 

app = FastAPI()
### This would disable the automatic docs generation
##app = FastAPI(docs_url=None, redoc_url=None)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

### I want the post in the below format
# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True # optional field with default value True
    


## Database CONNECTION WOULD GO HERE I am using  POSTGRESQL in production. connection for using Raw SQL queries

# try:
#     con=psycopg.connect(
#     host="localhost",
#     dbname= "FAST-API",
#     user= "postgres",
#     password= "2004065", row_factory=dict_row)
#     cursor=con.cursor()
#     print("DataBase connection was successful")
# except Exception as error:
#     print("Connecting to database failed")
#     print("Error:", error)
    
### Creating temporary in-memory database which is a list of dictionaries
# Using a type hint to specify that my_posts is a list of dictionaries
my_posts: List[dict] = [] # each time we create a post it will be added to this list and will be lost when the server restarts


### Including the routers for posts and users which we have created in the routers folder and linking them to the main FastAPI app
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)



### The api will start from GET method then find out forward slash (/) in the url and execute the function below by default method is GET
@app.get("/", status_code=status.HTTP_200_OK)
async def read_root():
    return {"Message": "This is my first FastAPI application!!!!"}
