import email
from .database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship




class PostModel(Base):
    #__tablename__ = "posts1" ###  posts for Raw SQL,  Post1 for SQLAlchemy ORM  then  Join operaiion add kora hoise
    __tablename__ = "posts_alembic" ### Alembic er jonno

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE',nullable=False)
    date=Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey("users_alembic.id", ondelete="CASCADE"), nullable=False)
    user_info= relationship("UserModel")


class UserModel(Base):
    #__tablename__ = "users" ### users for Raw SQL,  users1 for SQLAlchemy ORM  then  Join operaiion add kora hoise
    __tablename__ = "users_alembic"  ### Alembic er jonno

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    #users_phone_numbers = Column(String, nullable=True) ### New field add kora hoise optional hisabe testing alembic er jonno
    date=Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    #testing=Column(String, nullable=True)  ### New field add kora hoise optional hisabe testing alembic er jonno


class VoteModel(Base):
   # __tablename__ = "votes" ## votes for Raw SQL, votes1 for SQLAlchemy ORM  then  Join operaiion add kora hoise
    __tablename__ = "votes_alembic"  ### Alembic er jonno

    # user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    # post_id = Column(Integer, ForeignKey("posts1.id", ondelete="CASCADE"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users_alembic.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts_alembic.id", ondelete="CASCADE"), primary_key=True)
