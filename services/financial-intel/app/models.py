from typing import Optional
from sqlmodel import SQLModel, Field


class FinancialsFunding(SQLModel, table=True):
    __tablename__ = "financials_funding"

    company_id: int = Field(primary_key=True)

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
