from typing import Any
from sqlmodel import Session
from ..models import CompetitiveIntelligence


class CompetitiveRepository:

    @staticmethod
    def get_competitive(company_id: int, session: Session):
        return session.get(CompetitiveIntelligence, company_id)

    @staticmethod
    def upsert_competitive(
        company_id: int,
        data: dict[str, Any],
        session: Session
    ):
        obj = session.get(CompetitiveIntelligence, company_id)

        if obj:
            for k, v in data.items():
                setattr(obj, k, v)
        else:
            obj = CompetitiveIntelligence(company_id=company_id, **data)
            session.add(obj)

        return obj
