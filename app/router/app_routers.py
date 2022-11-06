from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.db_config import engine, get_db
from app.model import models
from app.repository.repositories import OwnerRepository, PetTypeRepository, PetRepository
from app.schema import schemas

app_router = APIRouter()

models.Base.metadata.create_all(bind=engine)


# OWNERS

@app_router.get("/")
async def root():
    return {"message": "Hello To VetApp"}


@app_router.get("/owners", response_model=list[schemas.Owner], tags=["owners"])
async def get_all_owners(db: Session = Depends(get_db)):
    return OwnerRepository.get_owners(db)


@app_router.post("/owners", response_model=schemas.Owner, tags=["owners"], status_code=201)
async def save_owners(db: Session = Depends(get_db), owner: schemas.OwnerCreate = None):
    return OwnerRepository.save(db, owner)


@app_router.get("/owners/document", response_model=schemas.Owner, tags=["owners"])
async def get_owners_by_document(document_type: str, document_number: str, db: Session = Depends(get_db)):
    return OwnerRepository.find_by_document(db, document_type, document_number)


@app_router.put("/owners", response_model=schemas.Owner, tags=["owners"])
async def update_owner(
        document_type: str,
        document_number: str,
        db: Session = Depends(get_db),
        owner: schemas.OwnerCreate = None):
    return OwnerRepository.update_by_document(db, document_type, document_number, owner)


@app_router.delete("/owners", status_code=204, tags=["owners"])
async def delete_owner(
        document_type: str,
        document_number: str,
        db: Session = Depends(get_db)):
    OwnerRepository.delete_by_document(db, document_type, document_number)


# PET TYPE

@app_router.get("/pet_types", response_model=list[schemas.PetType], tags=["pet types"])
async def get_pet_types(db: Session = Depends(get_db)):
    return PetTypeRepository.find_all(db)


# PET
@app_router.get("/pets", response_model=list[schemas.Pet], tags=["pets"])
async def get_pets(db: Session = Depends(get_db)):
    return PetRepository.find_all(db)


@app_router.post("/pets", response_model=schemas.Pet, tags=["pets"])
async def save_petpet_req(db: Session = Depends(get_db), pet_req: schemas.PetCreate = None):
    return PetRepository.save(db, pet_req)
