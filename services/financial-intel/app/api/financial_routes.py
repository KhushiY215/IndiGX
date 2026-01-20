from fastapi import APIRouter, HTTPException
from ..database import get_session
from ..repository.financial_repository import FinancialRepository
from ..schemas.financial_funding import (
    FinancialsFundingUpdate,
    FinancialsFundingRead
)

router = APIRouter(prefix="/financials", tags=["Financial Intelligence"])


# ============================================================
# GET — READ FINANCIAL DATA
# ============================================================

@router.get("/{company_id}", response_model=FinancialsFundingRead)
def get_financials(company_id: int):
    with get_session() as session:
        obj = FinancialRepository.get_financials(company_id, session)
        if not obj:
            raise HTTPException(
                status_code=404,
                detail="Financial data not found"
            )
        return obj


# ============================================================
# PUT — UPSERT FINANCIAL DATA
# ============================================================

@router.put("/{company_id}", response_model=FinancialsFundingRead)
def update_financials(
    company_id: int,
    payload: FinancialsFundingUpdate
):
    with get_session() as session:
        obj = FinancialRepository.upsert_financials(
            company_id,
            payload.dict(exclude_unset=True),
            session
        )
        session.commit()
        session.refresh(obj)
        return obj
