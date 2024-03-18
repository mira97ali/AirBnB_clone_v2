#!/usr/bin/python3
"""This module defines a class User"""
import sqlalchemy
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"

    email = sqlalchemy.Column(
        sqlalchemy.String(128),
        nullable=False)
    password = sqlalchemy.Column(
        sqlalchemy.String(128),
        nullable=False)
    first_name = sqlalchemy.Column(
        sqlalchemy.String(128))
    last_name = sqlalchemy.Column(
        sqlalchemy.String(128))
    places = relationship(
        "Place",
        cascade="all, delete, delete-orphan",
        backref="user")
