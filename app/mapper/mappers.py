from app.model import models
from app.schema import schemas


class OwnerMapper:

    @staticmethod
    def owner_schema_to_owner(owner_schema: schemas.Owner):
        return models.Owner(
            document_type=owner_schema.document_type,
            document_number=owner_schema.document_number,
            names=owner_schema.names,
            surnames=owner_schema.surnames,
            age=owner_schema.age,
            email=owner_schema.email,
            address=owner_schema.address,
            cellphone=owner_schema.cellphone,
            phone_number=owner_schema.phone_number
        )

    @staticmethod
    def owner_to_owner_schema(owner: models.Owner):
        return models.Owner(
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
