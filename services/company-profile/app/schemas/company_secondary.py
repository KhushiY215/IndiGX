from pydantic import BaseModel

class CompanySecondaryBase(BaseModel):
    twitter_handle: str | None = None
    facebook_page_url: str | None = None
    instagram_page_url: str | None = None
    key_business_leaders_name: str | None = None
    key_business_leaders_linkedin_url: str | None = None
    regulatory_licenses_certifications: str | None = None
    compliance_track_record: str | None = None
    legal_issues_controversies: str | None = None
    processing_time: str | None = None
    success_rate: str | None = None


class CompanySecondaryUpdate(CompanySecondaryBase):
    pass


class CompanySecondaryRead(CompanySecondaryBase):
    company_id: int

    class Config:
        from_attributes = True
