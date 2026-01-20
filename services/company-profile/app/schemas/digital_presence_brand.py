from pydantic import BaseModel

class DigitalPresenceBrandBase(BaseModel):
    quality_of_website: str | None = None
    awards_recognition: str | None = None
    brand_sentiment_score: str | None = None
    news_about_company: str | None = None
    average_deal_size: str | None = None
    top_customers: str | None = None
    website_traffic_rank: str | None = None
    social_media_followers_combined: str | None = None
    glassdoor_rating: str | None = None
    indeed_rating: str | None = None
    google_reviews_rating: str | None = None


class DigitalPresenceBrandUpdate(DigitalPresenceBrandBase):
    pass


class DigitalPresenceBrandRead(DigitalPresenceBrandBase):
    company_id: int

    class Config:
        from_attributes = True
