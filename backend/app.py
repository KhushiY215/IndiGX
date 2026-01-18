from fastapi import FastAPI
from backend.api import company_secondary_routes
from backend.api.company_full_profile import router as company_router
from backend.api.company_secondary_routes import router as company_secondary_router
from backend.api.competitive_intelligence_routes import router as competitive_intelligence_router
from backend.api.contact_information_routes import router as contact_information_router
from backend.api.digital_presence_brand_routes import router as digital_presence_brand_router
from backend.api.financials_funding_routes import router as financials_funding_router
from backend.api.indygx_assessment_routes import router as indygx_assessment_router
from backend.api.partnerships_ecosystem_routes import router as partnerships_ecosystem_router


app = FastAPI(
    title="IndyGX Company Intelligence API",
    version="1.0.0",
)

@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok"}

# Register routers
app.include_router(
    company_router,
    prefix="/companies",
    tags=["companies"]
)
 
# ...
# Rest of the code
app.include_router(
    company_secondary_router,
    prefix="/company-secondary",
    tags=["company-secondary"]
)

app.include_router(
    competitive_intelligence_router,
    prefix="/competitive-intelligence",
    tags=["competitive-intelligence"]
)

app.include_router(
    contact_information_router,
    prefix="/contact-information",
    tags=["Contact Information"]
)

app.include_router(
    digital_presence_brand_router,
    prefix="/digital-presence-brand",
    tags=["Digital Presence Brand"]
)

app.include_router(
    financials_funding_router,
    prefix="/financials-funding",
    tags=["Financials & Funding"]
)

app.include_router(
    indygx_assessment_router,
    prefix="/indygx-assessment",
    tags=["IndyGX Assessment"]
)

app.include_router(
    partnerships_ecosystem_router,
    prefix="/partnerships-ecosystem",
    tags=["Partnerships & Ecosystem"]
)
