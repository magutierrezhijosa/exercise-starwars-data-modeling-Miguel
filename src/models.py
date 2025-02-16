import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String , DateTime ,Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
    
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer,primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_planet = Column(Integer, ForeignKey('planet.id'))
    id_vehicle = Column(Integer, ForeignKey('vehicle.id'))
    id_character = Column(Integer, ForeignKey('character.id'))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    user_name = Column(String(20), nullable=False )
    first_name = Column(String(20), nullable=False )
    last_name = Column(String(20), nullable=False )
    email = Column(String(50), nullable=False )
    relation_favorite = relationship('Favorite' , backref='user')
    

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer,primary_key=True)
    relation_favorite = relationship('Favorite' , backref='planet')
    climate = Column(String(10), nullable=False )
    created = Column(DateTime, nullable=False )
    diameter = Column(Integer, nullable=False )
    edited = Column(DateTime, nullable=False )
    films = Column(String(200), nullable=False )
    gravity = Column(Integer, nullable=False )
    name = Column(String(30), nullable=False ) 
    orbital_period = Column(Integer, nullable=False )
    population = Column(Integer, nullable=False )
    residents = Column(String(200), nullable=False )
    rotation_period = Column(Integer, nullable=False )
    surface_water = Column(Integer, nullable=False )
    terrain = Column(String(20), nullable=False ) 
    url = Column(String(200), nullable=False )

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer,primary_key=True)
    birth_year = Column(String(10), nullable=False )
    eye_color = Column(String(10), nullable=False )
    gender = Column(String(10), nullable=False )
    hair_color = Column(String(10), nullable=False )
    height = Column(Integer, nullable=False )
    homeworld = Column(String(200), nullable=False )
    mass = Column(Integer, nullable=False )
    name = Column(String(30), nullable=False ) 
    skin_color = Column(String(30), nullable=False )
    created = Column(DateTime, nullable=False )
    edited = Column(DateTime, nullable=False )
    species = Column(String(200), nullable=False )
    starships = Column(String(200), nullable=False )
    url = Column(String(200), nullable=False ) 
    vehicles = Column(String(200), nullable=False )
    films = Column(String(200), nullable=False )
    relation_favorite = relationship('Favorite' , backref='character')

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer,primary_key=True)
    relation_favorite = relationship('Favorite' , backref='vehicle')
    cargo_capacity = Column(Integer, nullable=False )
    consumables = Column(String(20), nullable=False )
    cost_in_credits = Column(Float, nullable=False )
    created = Column(DateTime, nullable=False )
    crew = Column(Integer, nullable=False )
    edited = Column(DateTime, nullable=False )
    length = Column(Float, nullable=False )
    manufacturer = Column(String(40), nullable=False )
    max_atmosphering_speed = Column(Integer, nullable=False )
    model = Column(String(30), nullable=False )
    name = Column(String(30), nullable=False )
    passengers = Column(Integer, nullable=False )
    pilots = Column(String(100), nullable=False ) 
    films = Column(String(200), nullable=False ) 
    url = Column(String(200), nullable=False ) 
    vehicle_class = Column(String(20), nullable=False )
    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e