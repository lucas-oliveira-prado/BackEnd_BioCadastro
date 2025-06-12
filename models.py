from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from db import Base

class Animal(Base):
    __tablename__ = 'animal'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    sexo = Column(Integer)
    raca = Column(Integer)
    data_nascimento = Column(DateTime)
    status = Column(Integer)

class Vacinacao(Base):
    __tablename__ = 'vacinacao'
    
    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey('animal.id'))
    nome = Column(String(100))
    data = Column(DateTime)

class Pesagem(Base):
    __tablename__ = 'pesagem'
    
    id = Column(Integer, primary_key=True)
    id_animal = Column(Integer, ForeignKey('animal.id'))
    peso = Column(Float(8,2))
    data = Column(DateTime)
