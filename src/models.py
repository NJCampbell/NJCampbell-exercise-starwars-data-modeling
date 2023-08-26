import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    username = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)

    def serialize(self):
        return{
            "email": self.email,
            "username": self.username,
        }

class Planets(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    diameter = Column(String(30), nullable=False)
    rotation_period = Column(String(30), nullable=False)
    orbital_period = Column(String(30), nullable=False)
    gravity = Column(String(30), nullable=False)
    population = Column(String(30), nullable=False)
    climate = Column(String(30), nullable=False)
    terrain = Column(String(30), nullable=True)
    description = Column(String(30), nullable=True)
    
    def serialize(self):
        return{
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "description": self.description
        }
    
class Vehicles(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    model = Column(String(50), nullable=False)
    vehicle_class = Column(String(50), nullable=True)
    manufacturer = Column(String(50), nullable=True)
    cost_in_credits = Column(String(50), nullable=True)
    length = Column(String(50), nullable=True)
    crew = Column(String(50), nullable=True)
    passengers = Column(String(50), nullable=True)
    
    def serialize(self):
        return{
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers
        }

class Characters(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(String(50), nullable=True)
    mass = Column(String(50), nullable=True)
    hair_color = Column(String(50), nullable=True)
    skin_color = Column(String(50), nullable=True)
    eye_color = Column(String(50), nullable=True)
    gender = Column(String(50), nullable=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    planet = relationship(Planets)
    vehicle = relationship(Vehicles)
    
    def serialize(self):
        return{
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id
        }
    
class Favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=True)

    user = relationship(User)
    characters = relationship(Characters)
    planets = relationship(Planets)
    vehicles = relationship(Vehicles)
    

    def serialize(self):
        return{
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id
        }
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')