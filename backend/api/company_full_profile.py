from fastapi import APIRouter, HTTPException
from backend.repository.company_repository import CompanyRepository
from ..repository.company_repository import CompanyRepository
from ..schemas.company_full_profile import CompanyListItem, CompanyFullProfile

router = APIRouter()

@router.get("/")
def list_companies():
    """
    List all companies (id + name).
    """
    return CompanyRepository.list_companies()

@router.get("/{company_id}")
def get_company(company_id: int):
    """
    Get basic company info by ID.
    """
    company = CompanyRepository.get_company_by_id(company_id)

    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    return company


@router.get("/{company_id}/full-profile", response_model=CompanyFullProfile)
def get_full_profile(company_id: int):
    company = CompanyRepository.get_company_full_profile(company_id)
    if not company:
        raise HTTPException(status_code=404)
    return company