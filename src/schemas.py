from datetime import date
from pydantic import BaseModel, Field, ConfigDict, EmailStr


class ContactModel(BaseModel):
    name: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    email: str = EmailStr
    phone_number: str = Field(max_length=50)
    birstday: date
    notes: str = Field(max_length=500)


class ContactUpdate(ContactModel):
    done: bool


class ContactResponse(ContactModel):
    id: int
    name: str
    surname: str
    email: str
    phone_number: str
    birstday: date
    model_config = ConfigDict(from_attributes=True)
