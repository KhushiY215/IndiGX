from pydantic import BaseModel


class IndygxAssessmentBase(BaseModel):
    previous_interactions_with_indygx: str | None = None
    partnership_potential_rating: str | None = None
    collaboration_opportunity_score: str | None = None
    complementary_services_match_score: str | None = None


class IndygxAssessmentUpdate(IndygxAssessmentBase):
    pass


class IndygxAssessmentRead(IndygxAssessmentBase):
    company_id: int

    class Config:
        from_attributes = True
