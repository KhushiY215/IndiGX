from typing import Optional
from sqlmodel import SQLModel, Field


class ContactInformation(SQLModel, table=True):
    __tablename__ = "contact_information"

    company_id: int = Field(primary_key=True)

    contact_email: Optional[str] = None
    phone_number: Optional[str] = None
    primary_contact_person_name: Optional[str] = None
    primary_contact_person_title: Optional[str] = None
    primary_contact_person_email: Optional[str] = None
    primary_contact_person_phone_number: Optional[str] = None
    decision_maker_accessibility: Optional[str] = None
