from pydantic import BaseModel


class PartnershipsEcosystemBase(BaseModel):
    corporate_partnership_programs: str | None = None
    university_academic_partnerships: str | None = None
    industry_associations_memberships: str | None = None
    strategic_partnerships: str | None = None
    rd_investment_percentage: str | None = None
    technology_partners: str | None = None


class PartnershipsEcosystemUpdate(PartnershipsEcosystemBase):
    pass


class PartnershipsEcosystemRead(PartnershipsEcosystemBase):
    company_id: int

    class Config:
        from_attributes = True
