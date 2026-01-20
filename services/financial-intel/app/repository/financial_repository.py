from typing import Any
from sqlmodel import Session
from ..models import FinancialsFunding


class FinancialRepository:

    @staticmethod
    def get_financials(company_id: int, session: Session):
        return session.get(FinancialsFunding, company_id)

    @staticmethod
    def upsert_financials(
        company_id: int,
        data: dict[str, Any],
        session: Session
    ):
        obj = session.get(FinancialsFunding, company_id)

        if obj:
            for k, v in data.items():
                setattr(obj, k, v)
        else:
            obj = FinancialsFunding(company_id=company_id, **data)
            session.add(obj)

        return obj
