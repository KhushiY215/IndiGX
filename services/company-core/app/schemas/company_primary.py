from pydantic import BaseModel

class CompanyPrimaryBase(BaseModel):
    type: str | None = None
    company_name: str | None = None
    year_of_incorporation: str | None = None
    industry_segment: str | None = None
    nature_of_company: str | None = None
    website_url: str | None = None
    linkedin_profile_url: str | None = None
    ceo_name: str | None = None
    ceo_linkedin_url: str | None = None
    employee_size: str | None = None
    services_offerings: str | None = None
    core_value_proposition: str | None = None
    focus_sectors_industries: str | None = None
    countries_operating_in: str | None = None
    geographic_coverage_india: str | None = None

class CompanyPrimaryCreateUpdate(CompanyPrimaryBase):
    pass

class CompanyPrimaryRead(CompanyPrimaryBase):
    company_id: int

    class Config:
        from_attributes = True
