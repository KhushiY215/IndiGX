from typing import Any
from sqlmodel import Session, select, func
from ..models import CompanyPrimary

class CompanyRepository:

    @staticmethod
    def get_company_by_id(company_id: int, session: Session):
        stmt = select(CompanyPrimary).where(
            CompanyPrimary.company_id == company_id
        )
        return session.exec(stmt).first()

    @staticmethod
    def get_company_full_profile(company_id: int, session: Session):
        stmt = select(CompanyPrimary).where(
            CompanyPrimary.company_id == company_id
        )
        company = session.exec(stmt).first()

        if not company:
            return None

        # force-load relationships
        _ = company.secondary
        _ = company.competitive_intelligence
        _ = company.contact_information
        _ = company.digital_presence_brand
        _ = company.financials_funding
        _ = company.indygx_assessment
        _ = company.partnerships_ecosystem

        return company

    @staticmethod
    def upsert(
        company_id: int,
        data: dict[str, Any],
        session: Session
    ) -> CompanyPrimary:

        data["company_id"] = company_id

        stmt = select(CompanyPrimary).where(
            CompanyPrimary.company_id == company_id
        )
        existing = session.exec(stmt).one_or_none()

        if existing:
            for field, value in data.items():
                setattr(existing, field, value)
            session.add(existing)
            return existing

        new_company = CompanyPrimary(**data)
        session.add(new_company)
        return new_company
