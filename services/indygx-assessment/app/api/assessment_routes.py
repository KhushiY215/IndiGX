from fastapi import APIRouter, HTTPException
from ..database import get_session
from ..repository.assessment_repository import AssessmentRepository
from ..schemas.indygx_assessment import (
    IndygxAssessmentUpdate,
    IndygxAssessmentRead
)

router = APIRouter(
    prefix="/assessment",
    tags=["IndyGX Assessment"]
)

# ============================================================
# GET — READ INTERNAL ASSESSMENT
# ============================================================

@router.get("/{company_id}", response_model=IndygxAssessmentRead)
def get_assessment(company_id: int):
    with get_session() as session:
        obj = AssessmentRepository.get_assessment(company_id, session)
        if not obj:
            raise HTTPException(
                status_code=404,
                detail="IndyGX assessment not found"
            )
        return obj


# ============================================================
# PUT — UPSERT ASSESSMENT DATA
# ============================================================

@router.put("/{company_id}", response_model=IndygxAssessmentRead)
def update_assessment(
    company_id: int,
    payload: IndygxAssessmentUpdate
):
    with get_session() as session:
        obj = AssessmentRepository.upsert_assessment(
            company_id,
            payload.dict(exclude_unset=True),
            session
        )
        session.commit()
        session.refresh(obj)
        return obj
