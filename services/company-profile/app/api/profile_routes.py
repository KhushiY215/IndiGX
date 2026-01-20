from fastapi import APIRouter, HTTPException
from ..database import get_session
from ..repository.profile_repository import ProfileRepository
from ..schemas.company_secondary import (
    CompanySecondaryUpdate,
    CompanySecondaryRead
)
from ..schemas.digital_presence_brand import (
    DigitalPresenceBrandUpdate,
    DigitalPresenceBrandRead
)

router = APIRouter(prefix="/profiles", tags=["Company Profile"])

# ============================================================
# GET ROUTES (PUBLIC READ)
# ============================================================

@router.get("/{company_id}/secondary", response_model=CompanySecondaryRead)
def get_secondary(company_id: int):
    with get_session() as session:
        obj = ProfileRepository.get_secondary(company_id, session)
        if not obj:
            raise HTTPException(
                status_code=404,
                detail="Secondary profile not found"
            )
        return obj


@router.get("/{company_id}/digital", response_model=DigitalPresenceBrandRead)
def get_digital(company_id: int):
    with get_session() as session:
        obj = ProfileRepository.get_digital(company_id, session)
        if not obj:
            raise HTTPException(
                status_code=404,
                detail="Digital presence not found"
            )
        return obj


# ============================================================
# PUT ROUTES (ADMIN / INTERNAL UPDATE)
# ============================================================

@router.put("/{company_id}/secondary", response_model=CompanySecondaryRead)
def update_secondary(
    company_id: int,
    payload: CompanySecondaryUpdate
):
    with get_session() as session:
        obj = ProfileRepository.upsert_secondary(
            company_id,
            payload.dict(exclude_unset=True),
            session
        )
        session.commit()
        session.refresh(obj)
        return obj


@router.put("/{company_id}/digital", response_model=DigitalPresenceBrandRead)
def update_digital(
    company_id: int,
    payload: DigitalPresenceBrandUpdate
):
    with get_session() as session:
        obj = ProfileRepository.upsert_digital(
            company_id,
            payload.dict(exclude_unset=True),
            session
        )
        session.commit()
        session.refresh(obj)
        return obj
