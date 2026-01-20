from typing import Optional
from sqlmodel import SQLModel, Field


class PartnershipsEcosystem(SQLModel, table=True):
    __tablename__ = "partnerships_ecosystem"

    company_id: int = Field(primary_key=True)

    corporate_partnership_programs: Optional[str] = None
    university_academic_partnerships: Optional[str] = None
    industry_associations_memberships: Optional[str] = None
    strategic_partnerships: Optional[str] = None
    rd_investment_percentage: Optional[str] = None
    technology_partners: Optional[str] = None
