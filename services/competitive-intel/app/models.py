from typing import Optional
from sqlmodel import SQLModel, Field


class CompetitiveIntelligence(SQLModel, table=True):
    __tablename__ = "competitive_intelligence"

    company_id: int = Field(primary_key=True)

    competitors: Optional[str] = None
    unique_differentiators: Optional[str] = None
    competitive_advantages: Optional[str] = None
    weakness_gaps_in_offering: Optional[str] = None
    key_challenges_and_needs: Optional[str] = None
