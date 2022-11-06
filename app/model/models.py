from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship, backref

from app.config.db_config import Base


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    qty = Column(Float(asdecimal=True))
    partial = Column(Float(asdecimal=True))
    unit_measurement = Column(String(10))


class Owner(Base):
    __tablename__ = 'owner'

    id = Column(Integer, primary_key=True)
    document_type = Column(String(45))
    document_number = Column(String(45))
    names = Column(String(45))
    surnames = Column(String(45))
    age = Column(Integer)
    email = Column(String(60))
    address = Column(String(100))
    cellphone = Column(String(45))
    phone_number = Column(String(45))


class PetType(Base):
    __tablename__ = 'pet_type'

    id = Column(Integer, primary_key=True)
    type = Column(String(45))


class Pet(Base):
    __tablename__ = 'pet'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    age = Column(Integer)
    breed = Column(String(45))
    identification_number = Column(String(45))
    owner_id = Column(ForeignKey('owner.id'), nullable=False, index=True)
    pet_type_id = Column(ForeignKey('pet_type.id'), nullable=False, index=True)

    owner = relationship('Owner', cascade="all")
    pet_type = relationship('PetType')


class Visit(Base):
    __tablename__ = 'visit'

    id = Column(Integer, primary_key=True)
    reason = Column(Text)
    cost = Column(Float(asdecimal=True))
    pet_id = Column(ForeignKey('pet.id'), nullable=False, index=True)

    pet = relationship('Pet')


class Treatment(Base):
    __tablename__ = 'treatment'

    id = Column(Integer, primary_key=True)
    detail = Column(Text)
    total = Column(Float(asdecimal=True))
    visit_id = Column(ForeignKey('visit.id'), nullable=False, index=True)

    visit = relationship('Visit')


class Vet(Base):
    __tablename__ = 'vet'

    id = Column(Integer, primary_key=True)
    names = Column(String(45))
    surnames = Column(String(45))
    cellphone = Column(String(45))
    email = Column(String(45))
    visit_id = Column(ForeignKey('visit.id'), nullable=False, index=True)

    visit = relationship('Visit')


class TreatmentDetail(Base):
    __tablename__ = 'treatment_detail'

    id = Column(Integer, primary_key=True)
    qty = Column(Float(5, True))
    price = Column(Float(10, True))
    partial = Column(Float(10, True))
    treatment_id = Column(ForeignKey('treatment.id'), nullable=False, index=True)
    item_id = Column(ForeignKey('item.id'), nullable=False, index=True)

    item = relationship('Item')
    treatment = relationship('Treatment')
