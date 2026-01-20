from typing import Any
from sqlmodel import Session
from ..models import CompanySecondary, DigitalPresenceBrand


class ProfileRepository:

    # -------------------------
    # SECONDARY PROFILE
    # -------------------------

    @staticmethod
    def get_secondary(company_id: int, session: Session):
        return session.get(CompanySecondary, company_id)

    @staticmethod
    def upsert_secondary(
        company_id: int,
        data: dict[str, Any],
        session: Session
    ):
        obj = session.get(CompanySecondary, company_id)

        if obj:
            for k, v in data.items():
                setattr(obj, k, v)
        else:
            obj = CompanySecondary(company_id=company_id, **data)
            session.add(obj)

        return obj

    # -------------------------
    # DIGITAL PRESENCE
    # -------------------------

    @staticmethod
    def get_digital(company_id: int, session: Session):
        return session.get(DigitalPresenceBrand, company_id)

    @staticmethod
    def upsert_digital(
        company_id: int,
        data: dict[str, Any],
        session: Session
    ):
        obj = session.get(DigitalPresenceBrand, company_id)

        if obj:
            for k, v in data.items():
                setattr(obj, k, v)
        else:
            obj = DigitalPresenceBrand(company_id=company_id, **data)
            session.add(obj)

        return obj
