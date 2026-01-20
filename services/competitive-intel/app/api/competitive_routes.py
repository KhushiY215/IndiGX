from fastapi import APIRouter, HTTPException
from ..database import get_session
from ..repository.competitive_repository import CompetitiveRepository
from ..schemas.competitive_intelligence import (
    CompetitiveIntelligenceUpdate,
    CompetitiveIntelligenceRead
)

router = APIRouter(
    prefix="/competitive-intel",
    tags=["Competitive Intelligence"]
)

# ============================================================
# GET — READ STRATEGIC DATA
# ============================================================

@router.get("/{company_id}", response_model=CompetitiveIntelligenceRead)
def get_competitive(company_id: int):
    with get_session() as session:
        obj = CompetitiveRepository.get_competitive(company_id, session)
        if not obj:
            raise HTTPException(
                status_code=404,
                detail="Competitive intelligence not found"
            )
        return obj


# ============================================================
# PUT — UPSERT STRATEGIC DATA
# ============================================================

@router.put("/{company_id}", response_model=CompetitiveIntelligenceRead)
def update_competitive(
    company_id: int,
    payload: CompetitiveIntelligenceUpdate
):
    with get_session() as session:
        obj = CompetitiveRepository.upsert_competitive(
            company_id,
            payload.dict(exclude_unset=True),
            session
        )
        session.commit()
        session.refresh(obj)
        return obj
