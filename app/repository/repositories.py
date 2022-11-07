from sqlalchemy.orm import Session

from app.model import models
from app.model.models import Owner, Vet, Visit
from app.schema import schemas


class OwnerRepository:

    @staticmethod
    def get_owners(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Owner).offset(skip).limit(limit).all()

    @staticmethod
    def save(db: Session, owner: schemas.OwnerCreate):
        owner_model = models.Owner(
            document_type=owner.document_type,
            document_number=owner.document_number,
            names=owner.names,
            surnames=owner.surnames,
            age=owner.age,
            email=owner.email,
            address=owner.address,
            cellphone=owner.cellphone,
            phone_number=owner.phone_number
        )
        db.add(owner_model)
        db.commit()
        db.refresh(owner_model)
        return owner_model

    @staticmethod
    def find_by_document(db: Session, document_type: str, document_number: str):
        return db.query(models.Owner).filter_by(
            document_type=document_type,
            document_number=document_number
        ).first()

    @staticmethod
    def update_by_document(db: Session, document_type: str, document_number: str, owner_schema: schemas.OwnerCreate):
        owner = OwnerRepository.find_by_document(db, document_type, document_number)
        owner.document_number = owner_schema.document_number
        owner.document_type = owner_schema.document_type
        owner.names = owner_schema.names
        owner.surnames = owner_schema.surnames
        owner.email = owner_schema.email
        owner.phone_number = owner_schema.phone_number
        owner.age = owner_schema.age
        owner.address = owner_schema.address
        db.add(owner)
        db.commit()
        db.refresh(owner)
        return owner

    @staticmethod
    def delete_by_document(db: Session, document_type: str, document_number: str):
        db.query(models.Owner).filter_by(
            document_type=document_type,
            document_number=document_number
        ).delete()
        db.commit()


class PetTypeRepository:
    @staticmethod
    def find_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.PetType).offset(skip).limit(limit).all()

    @staticmethod
    def find_by_type(db: Session, pet_type: str):
        return db.query(models.PetType).filter_by(type=pet_type).first()


class PetRepository:

    @staticmethod
    def find_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Pet).offset(skip).limit(limit).all()

    @staticmethod
    def save(db: Session, pet_req: schemas.PetCreate):
        owner = pet_req.owner
        pet = models.Pet(
            name=pet_req.name,
            age=pet_req.age,
            breed=pet_req.breed,
            identification_number=pet_req.identification_number,
            owner=Owner(
                document_type=owner.document_type,
                document_number=owner.document_number,
                names=owner.names,
                surnames=owner.surnames,
                age=owner.age,
                email=owner.email,
                address=owner.address,
                cellphone=owner.cellphone,
                phone_number=owner.phone_number
            ),
            pet_type_id=pet_req.pet_type_id
        )
        db.add(pet)
        db.commit()
        db.refresh(pet)
        return pet


# VET
class VetRepository:
    @staticmethod
    def find_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Vet).offset(skip).limit(limit).all()

    @staticmethod
    def save(db: Session, vet_req=schemas.VetCreate):
        vet = Vet(
            document_type=vet_req.document_type,
            document_number=vet_req.document_number,
            names=vet_req.names,
            surnames=vet_req.surnames,
            cellphone=vet_req.cellphone,
            email=vet_req.email
        )
        db.add(vet)
        db.commit()
        db.refresh(vet)
        return vet


# ITEMS
class ItemRepository:
    @staticmethod
    def find_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Item).offset(skip).limit(limit).all()


# VISITS

class VisitRepository:

    @staticmethod
    def find_all(db: Session):
        return db.query(models.Visit).all()

    @staticmethod
    def save(db: Session, visit_req=schemas.VisitCreate):
        visit = Visit(
            reason=visit_req.reason,
            cost=visit_req.cost,
            pet_id=visit_req.pet_id,
            vet_id=visit_req.vet_id
        )
        db.add(visit)
        db.commit()
        db.refresh(visit)
        return visit
