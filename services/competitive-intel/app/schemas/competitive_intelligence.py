from pydantic import BaseModel


class CompetitiveIntelligenceBase(BaseModel):
    competitors: str | None = None
    unique_differentiators: str | None = None
    competitive_advantages: str | None = None
    weakness_gaps_in_offering: str | None = None
    key_challenges_and_needs: str | None = None


class CompetitiveIntelligenceUpdate(CompetitiveIntelligenceBase):
    pass


class CompetitiveIntelligenceRead(CompetitiveIntelligenceBase):
    company_id: int

    class Config:
        from_attributes = True
