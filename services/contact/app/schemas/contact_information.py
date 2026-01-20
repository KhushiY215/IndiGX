from pydantic import BaseModel


class ContactInformationBase(BaseModel):
    contact_email: str | None = None
    phone_number: str | None = None
    primary_contact_person_name: str | None = None
    primary_contact_person_title: str | None = None
    primary_contact_person_email: str | None = None
    primary_contact_person_phone_number: str | None = None
    decision_maker_accessibility: str | None = None


class ContactInformationUpdate(ContactInformationBase):
    pass


class ContactInformationRead(ContactInformationBase):
    company_id: int

    class Config:
        from_attributes = True
