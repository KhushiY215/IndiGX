from typing import Any
from sqlmodel import Session
from ..models import ContactInformation


class ContactRepository:

    @staticmethod
    def get_contact(company_id: int, session: Session):
        return session.get(ContactInformation, company_id)

    @staticmethod
    def upsert_contact(
        company_id: int,
        data: dict[str, Any],
        session: Session
    ):
        obj = session.get(ContactInformation, company_id)

        if obj:
            for k, v in data.items():
                setattr(obj, k, v)
        else:
            obj = ContactInformation(company_id=company_id, **data)
            session.add(obj)

        return obj
