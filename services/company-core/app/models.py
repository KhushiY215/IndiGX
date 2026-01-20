from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


# ============================================================
# ROOT TABLE FIRST (IMPORTANT FOR SQLMODEL)
# ============================================================

class CompanyPrimary(SQLModel, table=True):
    __tablename__ = "company_primary"

    company_id: int = Field(primary_key=True)

    type: Optional[str] = None
    company_name: Optional[str] = None
    year_of_incorporation: Optional[str] = None
    industry_segment: Optional[str] = None
    nature_of_company: Optional[str] = None
    website_url: Optional[str] = None
    linkedin_profile_url: Optional[str] = None
    ceo_name: Optional[str] = None
    ceo_linkedin_url: Optional[str] = None
    employee_size: Optional[str] = None
    services_offerings: Optional[str] = None
    core_value_proposition: Optional[str] = None
    focus_sectors_industries: Optional[str] = None
    countries_operating_in: Optional[str] = None
    geographic_coverage_india: Optional[str] = None

    secondary: Optional["CompanySecondary"] = Relationship(back_populates="company")
    competitive_intelligence: Optional["CompetitiveIntelligence"] = Relationship(back_populates="company")
    contact_information: Optional["ContactInformation"] = Relationship(back_populates="company")
    digital_presence_brand: Optional["DigitalPresenceBrand"] = Relationship(back_populates="company")
    financials_funding: Optional["FinancialsFunding"] = Relationship(back_populates="company")
    indygx_assessment: Optional["IndygxAssessment"] = Relationship(back_populates="company")
    partnerships_ecosystem: Optional["PartnershipsEcosystem"] = Relationship(back_populates="company")


# ============================================================
# DEPENDENT TABLES
# ============================================================

class CompanySecondary(SQLModel, table=True):
    __tablename__ = "company_secondary"

    company_id: int = Field(
        primary_key=True,
        foreign_key="company_primary.company_id"
    )

    twitter_handle: Optional[str] = None
    facebook_page_url: Optional[str] = None
    instagram_page_url: Optional[str] = None
    key_business_leaders_name: Optional[str] = None
    key_business_leaders_linkedin_url: Optional[str] = None
    regulatory_licenses_certifications: Optional[str] = None
    compliance_track_record: Optional[str] = None
    legal_issues_controversies: Optional[str] = None
    processing_time: Optional[str] = None
    success_rate: Optional[str] = None

    company: Optional["CompanyPrimary"] = Relationship(back_populates="secondary")


class CompetitiveIntelligence(SQLModel, table=True):
    __tablename__ = "competitive_intelligence"

    company_id: int = Field(
        primary_key=True,
        foreign_key="company_primary.company_id"
    )

    competitors: Optional[str] = None
    unique_differentiators: Optional[str] = None
    competitive_advantages: Optional[str] = None
    weakness_gaps_in_offering: Optional[str] = None
    key_challenges_and_needs: Optional[str] = None

    company: Optional["CompanyPrimary"] = Relationship(back_populates="competitive_intelligence")


class ContactInformation(SQLModel, table=True):
    __tablename__ = "contact_information"

    company_id: int = Field(
        primary_key=True,
        foreign_key="company_primary.company_id"
    )

    contact_email: Optional[str] = None
    phone_number: Optional[str] = None
    primary_contact_person_name: Optional[str] = None
    primary_contact_person_title: Optional[str] = None
    primary_contact_person_email: Optional[str] = None
    primary_contact_person_phone_number: Optional[str] = None
    decision_maker_accessibility: Optional[str] = None

    company: Optional["CompanyPrimary"] = Relationship(back_populates="contact_information")


class DigitalPresenceBrand(SQLModel, table=True):
    __tablename__ = "digital_presence_brand"

    company_id: int = Field(
        primary_key=True,
        foreign_key="company_primary.company_id"
    )

    quality_of_website: Optional[str] = None
    awards_recognition: Optional[str] = None
    brand_sentiment_score: Optional[str] = None
    news_about_company: Optional[str] = None
    average_deal_size: Optional[str] = None
    top_customers: Optional[str] = None
    website_traffic_rank: Optional[str] = None
    social_media_followers_combined: Optional[str] = None
    glassdoor_rating: Optional[str] = None
    indeed_rating: Optional[str] = None
    google_reviews_rating: Optional[str] = None

    company: Optional["CompanyPrimary"] = Relationship(back_populates="digital_presence_brand")


class FinancialsFunding(SQLModel, table=True):
    __tablename__ = "financials_funding"

    company_id: int = Field(
        primary_key=True,
        foreign_key="company_primary.company_id"
    )

    annual_revenues: Optional[str] = None
    annual_profits: Optional[str] = None
    company_valuation: Optional[str] = None
    year_over_year_growth_rate: Optional[str] = None
    profitability_status: Optional[str] = None
    market_share: Optional[str] = None
    key_investors_backers: Optional[str] = None
    exit_history: Optional[str] = None
    recent_funding_rounds: Optional[str] = None
    total_capital_raised: Optional[str] = None

    company: Optional["CompanyPrimary"] = Relationship(back_populates="financials_funding")


class IndygxAssessment(SQLModel, table=True):
    __tablename__ = "indygx_assessment"

    company_id: int = Field(
        primary_key=True,
        foreign_key="company_primary.company_id"
    )

    previous_interactions_with_indygx: Optional[str] = None
    partnership_potential_rating: Optional[str] = None
    collaboration_opportunity_score: Optional[str] = None
    complementary_services_match_score: Optional[str] = None

    company: Optional["CompanyPrimary"] = Relationship(back_populates="indygx_assessment")


class PartnershipsEcosystem(SQLModel, table=True):
    __tablename__ = "partnerships_ecosystem"

    company_id: int = Field(
        primary_key=True,
        foreign_key="company_primary.company_id"
    )

    corporate_partnership_programs: Optional[str] = None
    university_academic_partnerships: Optional[str] = None
    industry_associations_memberships: Optional[str] = None
    strategic_partnerships: Optional[str] = None
    rd_investment_percentage: Optional[str] = None
    technology_partners: Optional[str] = None

    company: Optional["CompanyPrimary"] = Relationship(back_populates="partnerships_ecosystem")
