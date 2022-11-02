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
