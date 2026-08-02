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


    products_count = Column(
        Integer
    )


    rating = Column(
        String
    )


    reviews = Column(
        Integer
    )


    description = Column(
        Text
    )


    product_type = Column(
        String
    )


    tax = Column(
        Float
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


    location = Column(
        String
    )


    price = Column(
        Integer
    )


    mileage = Column(
        String
    )


    year = Column(
        Integer
    )


    color = Column(
        String
    )


    body_type = Column(
        String
    )


    fuel = Column(
        String
    )


    transmission = Column(
        String
    )


    engine = Column(
        String
    )


    air_conditioning = Column(
        String
    )


    steering = Column(
        String
    )


    condition = Column(
        String
    )


    status = Column(
        String
    )


    created_date = Column(
        String
    )


    description = Column(
        Text
    )