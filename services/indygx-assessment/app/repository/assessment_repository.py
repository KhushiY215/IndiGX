from typing import Any
from sqlmodel import Session
from ..models import IndygxAssessment


class AssessmentRepository:

    @staticmethod
    def get_assessment(company_id: int, session: Session):
        return session.get(IndygxAssessment, company_id)

    @staticmethod
    def upsert_assessment(
        company_id: int,
        data: dict[str, Any],
        session: Session
    ):
        obj = session.get(IndygxAssessment, company_id)

        if obj:
            for k, v in data.items():
                setattr(obj, k, v)
        else:
            obj = IndygxAssessment(company_id=company_id, **data)
            session.add(obj)

        return obj
