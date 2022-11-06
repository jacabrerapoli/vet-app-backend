from pydantic.main import BaseModel


class OwnerBase(BaseModel):
    document_type: str
    document_number: str
    names: str
    surnames: str
    age: int
    email: str
    address: str
    cellphone: str
    phone_number: str


class OwnerCreate(OwnerBase):
    pass


class Owner(OwnerBase):
    id = int

    class Config:
        orm_mode = True


class PetTypeBase(BaseModel):
    id: int
    type: str


class PetTypeCreate(PetTypeBase):
    pass


class PetType(PetTypeBase):
    id = int

    class Config:
        orm_mode = True


class PetBase(BaseModel):
    name: str
    age: int
    breed: str
    identification_number: str
    owner: Owner
    pet_type: PetType


class PetCreate(BaseModel):
    name: str
    age: int
    breed: str
    identification_number: str
    owner: Owner
    pet_type_id: int


class Pet(PetBase):
    id = int

    class Config:
        orm_mode = True
