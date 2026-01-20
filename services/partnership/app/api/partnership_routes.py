from fastapi import APIRouter, HTTPException
from ..database import get_session
from ..repository.partnership_repository import PartnershipRepository
from ..schemas.partnerships_ecosystem import (
    PartnershipsEcosystemUpdate,
    PartnershipsEcosystemRead
)

router = APIRouter(
    prefix="/partnerships",
    tags=["Partnership & Ecosystem"]
)

# ============================================================
# GET — READ PARTNERSHIP DATA
# ============================================================

@router.get("/{company_id}", response_model=PartnershipsEcosystemRead)
def get_partnerships(company_id: int):
    with get_session() as session:
        obj = PartnershipRepository.get_partnerships(company_id, session)
        if not obj:
            raise HTTPException(
                status_code=404,
                detail="Partnership ecosystem data not found"
            )
        return obj


# ============================================================
# PUT — UPSERT PARTNERSHIP DATA
# ============================================================

@router.put("/{company_id}", response_model=PartnershipsEcosystemRead)
def update_partnerships(
    company_id: int,
    payload: PartnershipsEcosystemUpdate
):
    with get_session() as session:
        obj = PartnershipRepository.upsert_partnerships(
            company_id,
            payload.dict(exclude_unset=True),
            session
        )
        session.commit()
        session.refresh(obj)
        return obj
