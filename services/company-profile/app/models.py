from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class CompanySecondary(SQLModel, table=True):
    __tablename__ = "company_secondary"

    company_id: int = Field(primary_key=True)

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


class DigitalPresenceBrand(SQLModel, table=True):
    __tablename__ = "digital_presence_brand"

    company_id: int = Field(primary_key=True)

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
