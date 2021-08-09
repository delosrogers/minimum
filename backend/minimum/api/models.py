import sqlite3
import uuid
from minimum import db
from sqlalchemy import Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship


class Parent(db.Model):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    children = relationship("Child")


class Child(db.Model):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent.id"))


# class User(db.Model):
#     __tablename__ = "user"
#     id = Column(String, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     username = Column(String)
#     email = Column(String)
#     articles = relationship("article", back_populates="author")
#     comments = relationship("comment", back_populates="author")


# class Article(db.Model):
#     __tablename__ = "article"
#     id = Column(String, primary_key=True)
#     # author = relationship("User", back_populates="articles")
#     author_id = Column(String, ForeignKey("user.id"))
#     text = Text()
#     comments = relationship("comment", back_populates="article")
#     title = Column(String)


# class Comment(db.Model):
#     __tablename__ = "comment"
#     id = Column(String, primary_key=True)
#     # article = relationship("article", back_populates="comments")
#     article_id = Column(String, ForeignKey("article.id"))
#     # author = relationship("user", back_populates="comments")
#     author_id = Column(String, ForeignKey("user.id"))
#     text = Text()


# db.create_all()


# def add_article(title: str, text: str, author: str) -> str:
#     id = uuid.uuid4().bytes()
#     article = Article(id=id, author=author, text=text, title=title,)
#     db.session.add(article)
#     db.session.commit()
#     return id


# def get_article(id: str) -> dict:
#     Article.query.filter_by(id=id).first()


# def add_user(username, first_name=None, last_name=None, email=None) -> str:
#     id = uuid.uuid4().bytes
#     user = User(
#         id=id,
#         username=username,
#         first_name=first_name,
#         last_name=last_name,
#         email=email,
#     )
#     print(user)
#     return id

