import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    username = Column(String(20))
    firstname = Column(String(20))
    lastname = Column(String(20))
    email = Column(String(50), unique=True)

class Follower(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.ID'))
    user_to_id = Column(Integer, ForeignKey('user.ID'))
    user_relationship = relationship(User)
    user_relationship = relationship(User)
    

class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.ID'), unique=True)
    user_relationship = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    ID = Column(Integer, primary_key=True)
    type = Column(Integer, unique=True)
    url = Column(String(20))
    post_id = Column(Integer, ForeignKey('post.ID'))
    post_relationship = relationship(Post)


class Comment(Base):
    __tablename__ = 'comments'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(100))
    author_id = Column(Integer, ForeignKey('user.ID'))
    post_id = Column(Integer, ForeignKey('post.ID'))
    user_relationship = relationship(User)
    post_relationship = relationship(Post)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
