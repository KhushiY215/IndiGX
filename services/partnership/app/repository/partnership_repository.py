from typing import Any
from sqlmodel import Session
from ..models import PartnershipsEcosystem


class PartnershipRepository:

    @staticmethod
    def get_partnerships(company_id: int, session: Session):
        return session.get(PartnershipsEcosystem, company_id)

    @staticmethod
    def upsert_partnerships(
        company_id: int,
        data: dict[str, Any],
        session: Session
    ):
        obj = session.get(PartnershipsEcosystem, company_id)

        if obj:
            for k, v in data.items():
                setattr(obj, k, v)
        else:
            obj = PartnershipsEcosystem(company_id=company_id, **data)
            session.add(obj)

        return obj
