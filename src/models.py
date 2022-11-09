import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    password = Column(String(10),nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

class Personajes(Base):
    __tablename__= 'Personajes'
    id= Column(Integer, primary_key= True)
    planeta= Column(Integer, ForeignKey('Planetas.id'))
    birth_year= Column(Date)
    eye_color= Column(String(250)) 
    films= Column(String(250)) 
    gender= Column(String(250))
    hair_color= Column(String(250))
    height= Column(Integer) 
    mass= Column(Integer)
    skin_color= Column(String(250)) 
    
    
    # Planetas_relacion=relationship(Planetas)
    
class Planetas(Base):
    __tablename__='Planetas'
    id= Column(Integer, primary_key= True)
    nombre= Column(String(250))
    personaje=Column(Integer, ForeignKey('Personajes.id'))
    personajes= relationship(Personajes)
    climate= Column(String(250))
    diameter= Column(Float)
    gravity= Column(Integer)
    name= Column(String(250))
    orbital_period= Column(Integer)
    population= Column(Integer)
    rotation_period= Column(Integer)
    surface_water= Column(Integer)
    terrain= Column(String(250))
    

class Favoritos_Personajes(Base):
    __tablename__ = 'Favoritos_Personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id_user= Column(Integer, ForeignKey('Users.id'), primary_key=True)
    id_personaje= Column(Integer, ForeignKey('Personajes.id'), primary_key=True)
    user= relationship(Users)
    personaje = relationship(Personajes)

class Favoritos_Planetas(Base):
    __tablename__ = 'Favoritos_Planetas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id_user= Column(Integer, ForeignKey('Users.id'), primary_key=True)
    id_nave= Column(Integer, ForeignKey('Planetas.id'), primary_key=True)
    user= relationship(Users)
    Planetas = relationship(Planetas)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')