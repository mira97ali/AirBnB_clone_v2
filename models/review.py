#!/usr/bin/python3
""" Review module for the HBNB project """

import sqlalchemy

from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"

    text = sqlalchemy.Column(
        sqlalchemy.String(1024),
        nullable=False)
    place_id = sqlalchemy.Column(
        sqlalchemy.String(60),
        sqlalchemy.ForeignKey("places.id"), nullable=False)
    user_id = sqlalchemy.Column(
        sqlalchemy.String(60),
        sqlalchemy.ForeignKey("users.id"), nullable=False)
