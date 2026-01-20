from fastapi import APIRouter, HTTPException
from ..database import get_session
from ..repository.contact_repository import ContactRepository
from ..schemas.contact_information import (
    ContactInformationUpdate,
    ContactInformationRead
)

router = APIRouter(
    prefix="/contacts",
    tags=["Contact & Engagement"]
)

# ============================================================
# GET — READ CONTACT INFORMATION
# ============================================================

@router.get("/{company_id}", response_model=ContactInformationRead)
def get_contact(company_id: int):
    with get_session() as session:
        obj = ContactRepository.get_contact(company_id, session)
        if not obj:
            raise HTTPException(
                status_code=404,
                detail="Contact information not found"
            )
        return obj


# ============================================================
# PUT — UPSERT CONTACT INFORMATION
# ============================================================

@router.put("/{company_id}", response_model=ContactInformationRead)
def update_contact(
    company_id: int,
    payload: ContactInformationUpdate
):
    with get_session() as session:
        obj = ContactRepository.upsert_contact(
            company_id,
            payload.dict(exclude_unset=True),
            session
        )
        session.commit()
        session.refresh(obj)
        return obj
