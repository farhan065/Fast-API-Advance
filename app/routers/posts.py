
from .. import model , schemas, oauth2
from ..utils import hash_password
from ..database import engine, get_db
from fastapi import Depends, FastAPI, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional



router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)
# ### Using Database
# @app.get("/posts")
# def get_posts():
#     cursor.execute("SELECT * FROM posts")
#     posts = cursor.fetchall()
#     #print(posts)
#     return {"data": posts}

### Using SQLAlchemy ORM
# @app.get("/posts",response_model=List[schemas.PostResponse] ) ## @app er jaygay @router use korlam app tokhoni use kora jabe jokhon app=FastAPI() thakbe and eta alada file e ache tai router use korlam . eta main.py te include kora hobe
@router.get("/", response_model=List[schemas.PostOut]) ### using joint query to get posts along with vote counts
# def get_posts(db: Session = Depends(get_db)):
#     posts = db.query(model.PostModel).all()
#     return posts
### Using Database with OAuth2
# def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     print(f"Current user id: {current_user.email}")
#     posts = db.query(model.PostModel).all() ## ekhnae user shob post dekhte parbe
#     #posts = db.query(model.PostModel).filter(model.PostModel.user_id == current_user.id).all() ## ekhnae user sudhu nijer post guloi dekhte parbe
#     return posts

### using Query Parameters for limit and skip and search
# def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
#     print(f"Current user id: {current_user.email}")
#     posts = db.query(model.PostModel).filter(model.PostModel.title.contains(search)).limit(limit).offset(skip).all() ## ekhnae user sudhu nijer post guloi dekhte parbe
#     # results = db.query(model.PostModel, func.count(model.VoteModel.post_id).label("votes")).join(model.VoteModel, model.VoteModel.post_id == model.PostModel.id, isouter=True).group_by(model.PostModel.id).all()
#     # print(results)
#     return posts

### using joint query to get posts along with vote counts
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # print(f"Current user id: {current_user.email}")
    
    results = db.query(model.PostModel, func.count(model.VoteModel.post_id).label("votes")).join(
        model.VoteModel, model.VoteModel.post_id == model.PostModel.id, isouter=True).group_by(
        model.PostModel.id).filter(model.PostModel.title.contains(search)).limit(limit).offset(skip).all()
    
    return [{"Post": post, "votes": votes} for post, votes in results]



# @app.post("/posts", status_code=status.HTTP_201_CREATED)  eta use korle response object lagbe na
@router.post("/", response_model=schemas.PostResponse)
##This is where user can sent any data in the form of JSON
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     #return {"data": "Post created successfully"}
#     return {"Your Created Post": f"Post created with title: {payload['title']} and content: {payload['content']}"}

##Using Pydantic Model
# def create_posts(new_post: Post, response: Response):
#     # print(new_post.title)
#     # print(new_post.content)
#     # print(new_post.published)
#     # print(new_post.rating)
#     # print(new_post.dict()) # .dict() method converts the pydantic model to a dictionary
#     post_dict = new_post.dict()
#     post_dict['id'] = randrange(0, 1000000) # adding a random id to the post
#     my_posts.append(post_dict)   
#     response.status_code = status.HTTP_201_CREATED
#     return {"data": post_dict}


# ### Using Database
# def create_posts(new_post: Post, response: Response):
#     cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
#                    (new_post.title, new_post.content, new_post.published))
#     new_post = cursor.fetchone()
#     con.commit()
#     response.status_code = status.HTTP_201_CREATED
#     return {"data": new_post}

### Using SQLAlchemy ORM 
# def create_posts(new_post: schemas.PostCreate, db: Session = Depends(get_db)):
#     # post_model = model.PostModel(title=new_post.title, content=new_post.content, published=new_post.published)
#     # db.add(post_model)
#     # db.commit()
#     # db.refresh(post_model)

#     ### using unpacking method
#     post_model = model.PostModel(**new_post.dict())  # unpacking the dictionary
#     db.add(post_model)
#     db.commit()
#     db.refresh(post_model)
#     return post_model

### Using  oauth2 to get current user
def create_posts(new_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # post_model = model.PostModel(title=new_post.title, content=new_post.content, published=new_post.published)
    # db.add(post_model)
    # db.commit()
    # db.refresh(post_model)
    print(f"Current user id: {current_user.email}")

    ### using unpacking method
    post_model = model.PostModel(user_id=current_user.id, **new_post.dict())  # unpacking the dictionary
    db.add(post_model)
    db.commit()
    db.refresh(post_model)
    return post_model



    

## Get a specific post by id
# @router.get("/{id}", response_model=schemas.PostResponse)  ### get post with specific id
@router.get("/{id}", response_model=schemas.PostOut)  ### get post with vote counts with specific id
# def get_post(id: int, response: Response): 
#     for post in my_posts:
#         if post["id"]== id:
#             return {"post_detail": post}
    
#     # response.status_code = status.HTTP_404_NOT_FOUND
#     # return {"message": f"post with id: {id} was not found"}
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                         detail=f"post with id: {id} was not found")

### Using Database

# def get_post(id: int, response: Response):
#     cursor.execute("SELECT * FROM posts WHERE id = %s", (str(id),))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} was not found")
#     return {"post_detail": post}


### Using SQLAlchemy ORM
# def get_post(id: int, db: Session = Depends(get_db)):
#     post = db.query(model.PostModel).filter(model.PostModel.id == id).first()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} was not found")
#     return  post


#### Using  oauth2 to get current user
# def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     print(f"Current user id: {current_user.email}")

#     post = db.query(model.PostModel).filter(model.PostModel.id == id).first()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} was not found")
#     ### etar por user sudhu nijer post gulo access korte parbe
#     # if post.user_id != current_user.id:
#     #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
#     #                         detail=f"Not authorized to perform requested action")
#     return  post


### get post with vote counts with specific id
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    print(f"Current user id: {current_user.email}")
    post_with_votes = db.query(model.PostModel, func.count(model.VoteModel.post_id).label("votes")).join(
        model.VoteModel, model.VoteModel.post_id == model.PostModel.id, isouter=True).group_by(
        model.PostModel.id).filter(model.PostModel.id == id).first()    
    if not post_with_votes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {"Post": post_with_votes[0], "votes": post_with_votes[1]}


    
## Delete a specific post by id
@router.delete("/{id}")
# def delete_post(id: int, response: Response):
#     for post in my_posts:
#         if post["id"]== id:
#             my_posts.remove(post)
#             response.status_code = status.HTTP_204_NO_CONTENT
#             return {"message": "Post deleted successfully"}
    
#     response.status_code = status.HTTP_404_NOT_FOUND
#     return {"message": f"post with id: {id} was not found"}

### Using Database

# def delete_post(id: int, response: Response):
#     cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", (str(id),))
#     deleted_post = cursor.fetchone()
#     con.commit()
#     if deleted_post is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} was not found")
#     response.status_code = status.HTTP_204_NO_CONTENT
#     return {"message": "Post deleted successfully"}


### Using SQLAlchemy ORM
# def delete_post(id: int, db: Session = Depends(get_db)):
#     post = db.query(model.PostModel).filter(model.PostModel.id == id)
#     if post.first() is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} was not found")
#     post.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

### Using  oauth2 to get current user
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    print(f"Current user id: {current_user.email}")

    post = db.query(model.PostModel).filter(model.PostModel.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    if post.first().user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    
            
    
## Update a specific post by id
@router.put("/{id}", response_model=schemas.PostResponse)
# def update_post(id: int, updated_post: Post, response: Response):
#     for post in my_posts:
#         if post["id"]== id:
#             post.update(updated_post.dict())
#             response.status_code = status.HTTP_202_ACCEPTED
#             return {"message": "Post updated successfully"}
    
#     response.status_code = status.HTTP_404_NOT_FOUND
#     return {"message": f"post with id: {id} was not found"}

### Using Database

# def update_post(id: int, updated_post: Post, response: Response):
#     cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
#                    (updated_post.title, updated_post.content, updated_post.published, str(id)))
#     post = cursor.fetchone()
#     con.commit()
#     if post is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} was not found")
#     response.status_code = status.HTTP_202_ACCEPTED
#     return {"data": post}

### Using SQLAlchemy ORM
# def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
#     post_query = db.query(model.PostModel).filter(model.PostModel.id == id)
#     post = post_query.first()
#     if post is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} was not found")
#     post_query.update(updated_post.dict(), synchronize_session=False)
#     db.commit()
#     return post_query.first()


#### Using  oauth2 to get current user
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    print(f"Current user id: {current_user.email}")
    post_query = db.query(model.PostModel).filter(model.PostModel.id == id)
    post = post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()