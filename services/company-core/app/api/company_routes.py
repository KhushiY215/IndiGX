from fastapi import APIRouter, HTTPException
from sqlmodel import Session
from ..schemas.company_primary import (
    CompanyPrimaryCreateUpdate,
    CompanyPrimaryRead
)
from ..repository.company_repository import CompanyRepository
from ..database import get_session

router = APIRouter(prefix="/companies", tags=["Company Core"])

@router.get("/{company_id}", response_model=CompanyPrimaryRead)
def get_company(company_id: int):
    with get_session() as session:
        company = CompanyRepository.get_company_by_id(company_id, session)
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")
        return company

@router.put("/{company_id}", response_model=CompanyPrimaryRead)
def update_company(
    company_id: int,
    payload: CompanyPrimaryCreateUpdate
):
    with get_session() as session:
        company = CompanyRepository.upsert(
            company_id,
            payload.dict(exclude_unset=True),
            session
        )
        session.commit()
        session.refresh(company)
        return company
