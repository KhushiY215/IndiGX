from pydantic import BaseModel


class FinancialsFundingBase(BaseModel):
    annual_revenues: str | None = None
    annual_profits: str | None = None
    company_valuation: str | None = None
    year_over_year_growth_rate: str | None = None
    profitability_status: str | None = None
    market_share: str | None = None
    key_investors_backers: str | None = None
    exit_history: str | None = None
    recent_funding_rounds: str | None = None
    total_capital_raised: str | None = None


class FinancialsFundingUpdate(FinancialsFundingBase):
    pass


class FinancialsFundingRead(FinancialsFundingBase):
    company_id: int

    class Config:
        from_attributes = True
