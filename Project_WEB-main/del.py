from flask import Flask, render_template, redirect, abort, request
from data1 import db_session
from data1.recipes import Recipes
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
import random
from data1.users import User
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String

sqlite_database = 'db/recipes.db'
engine = create_engine(sqlite_database, echo=True)


class Base(DeclarativeBase): pass


class Person(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(bind=engine)

with Session(autoflush=False, bind=engine) as db:
    bob = db.query(Person).filter(Person.id == 1).first()
    db.delete(bob)  # удаляем объект
    db.commit()  # сохраняем изменения
