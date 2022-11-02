from sqlalchemy.orm import Session

from app.model import models
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
