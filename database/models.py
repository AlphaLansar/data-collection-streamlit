from sqlalchemy import Column, Integer, Float, String, Text

from .database import Base



# ==========================
# TABLE BOOKS
# ==========================

class Book(Base):

    __tablename__ = "books"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    title = Column(
        String,
        nullable=False
    )


    price = Column(
        Float
    )


    availability = Column(
        String
    )


    rating = Column(
        String
    )


    image = Column(
        String
    )


    url = Column(
        String
    )


    description = Column(
        Text
    )




# ==========================
# TABLE CARS
# ==========================

class Car(Base):

    __tablename__ = "cars"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    url = Column(
        String
    )


    title = Column(
        String
    )


    brand = Column(
        String
    )


    model = Column(
        String
    )


    year = Column(
        Integer
    )


    location = Column(
        String
    )


    region = Column(
        String
    )


    price = Column(
        Integer
    )


    mileage = Column(
        Integer
    )


    transmission = Column(
        String
    )